// =========================================================================
// КЛИЕНТСКИЙ НАКОПИТЕЛЬНЫЙ СКАНЕР ПОКЕМОНОВ ИЗ ПК (COBBLEMON)
// Горячая клавиша: F9 (или Shift + P) — Добавить / Обновить покемонов в базе
// Очистка базы: Shift + F9 (или Ctrl + F9)
// =========================================================================

let lastPCScanTime = 0
// Накопительная база покемонов (ключ: уникальный UUID покемона, чтобы исключить дубликаты)
let globalPokemonMap = {}

ClientEvents.tick(event => {
  let player = Client.player
  if (!player) return

  let mc = Java.loadClass('net.minecraft.client.Minecraft').getInstance()
  if (!mc || !mc.getWindow()) return

  let windowHandle = mc.getWindow().getWindow()
  let GLFW = Java.loadClass('org.lwjgl.glfw.GLFW')

  let isF9 = GLFW.glfwGetKey(windowHandle, 298) === 1
  let isP = GLFW.glfwGetKey(windowHandle, 80) === 1
  let isShift = GLFW.glfwGetKey(windowHandle, 340) === 1 || GLFW.glfwGetKey(windowHandle, 344) === 1
  let isCtrl = GLFW.glfwGetKey(windowHandle, 341) === 1 || GLFW.glfwGetKey(windowHandle, 345) === 1

  let now = Date.now()
  if (now - lastPCScanTime < 800) return

  // 1. ОЧИСТКА БАЗЫ (Shift + F9 или Ctrl + F9)
  if ((isShift || isCtrl) && isF9) {
    lastPCScanTime = now
    globalPokemonMap = {}
    player.tell('§c[PC Scanner] 🗑 База покемонов очищена! Теперь можно сканировать заново.')
    return
  }

  // 2. НАКОПИТЕЛЬНОЕ СКАНИРОВАНИЕ (F9 или Shift + P)
  if (isF9 || (isShift && isP)) {
    lastPCScanTime = now
    scanAndAccumulatePokemon(player)
  }
})

function scanAndAccumulatePokemon(player) {
  try {
    let CobblemonClient = Java.loadClass('com.cobblemon.mod.common.client.CobblemonClient').INSTANCE
    let storageManager = CobblemonClient.getStorage()
    if (!storageManager) {
      player.tell('§c[PC Scanner] ❌ Не удалось получить доступ к хранилищу Cobblemon.')
      return
    }

    let Stats = Java.loadClass('com.cobblemon.mod.common.api.pokemon.stats.Stats')
    let newlyFoundCount = 0
    let partyCount = 0
    let pcCount = 0

    // 1. СКАНИРОВАНИЕ КОМАНДЫ (Party - 6 слотов)
    let party = storageManager.getMyParty()
    if (party) {
      let partySlots = party.getSlots ? party.getSlots() : party
      let slotIdx = 1
      for (let p of partySlots) {
        if (p) {
          let uuidStr = String(p.getUuid ? p.getUuid() : `${p.species.name}_party_${slotIdx}`)
          if (!globalPokemonMap[uuidStr]) {
            newlyFoundCount++
          }
          globalPokemonMap[uuidStr] = serializePokemon(p, `Команда (Слот ${slotIdx})`, Stats, uuidStr)
        }
        slotIdx++
      }
    }

    // 2. СКАНИРОВАНИЕ КОРОБОК ПК (PC Boxes)
    let pcStores = storageManager.getPcStores()
    if (pcStores && !pcStores.isEmpty()) {
      for (let pcEntry of pcStores.values()) {
        let boxes = pcEntry.getBoxes()
        let boxNum = 1
        for (let box of boxes) {
          let slots = box.getSlots()
          let slotNum = 1
          for (let p of slots) {
            if (p) {
              let uuidStr = String(p.getUuid ? p.getUuid() : `${p.species.name}_box_${boxNum}_${slotNum}`)
              if (!globalPokemonMap[uuidStr]) {
                newlyFoundCount++
              }
              globalPokemonMap[uuidStr] = serializePokemon(p, `Коробка ${boxNum} (Слот ${slotNum})`, Stats, uuidStr)
            }
            slotNum++
          }
          boxNum++
        }
      }
    }

    let allPokemonList = Object.values(globalPokemonMap)
    if (allPokemonList.length === 0) {
      player.tell('§e[PC Scanner] ⚠️ Покемоны не найдены (откройте ПК в игре, чтобы клиент загрузил коробки)!')
      return
    }

    // Подсчёт итогов
    for (let p of allPokemonList) {
      if (p.location.includes('Команда')) {
        partyCount++
      } else {
        pcCount++
      }
    }

    // 3. СОХРАНЯЕМ НАКОПЛЕННЫЙ JSON
    let exportData = {
      scan_date: new Date().toISOString(),
      party_pokemon_count: partyCount,
      pc_pokemon_count: pcCount,
      total_pokemon_count: allPokemonList.length,
      pokemon: allPokemonList
    }

    let filePath = 'kubejs/my_cobblemon_pc.json'
    JsonIO.write(filePath, exportData)

    player.tell(`§a[PC Scanner] ✔ База пополнена (+${newlyFoundCount} новых)!`)
    player.tell(`§fВсего накоплено в базе: §e${allPokemonList.length} покемонов §f(Команда: §b${partyCount}§f, ПК: §e${pcCount}§f)`)
    player.tell(`§bФайл сохранён в: §f${filePath}`)
    player.tell(`§7[Подсказка: переключайте страницы ПК и нажимайте F9 — покемоны будут накапливаться!]`)
  } catch (e) {
    console.error(`[PC Scanner Error] ` + e)
    player.tell(`§c[PC Scanner Ошибка]: ` + e)
  }
}

function serializePokemon(p, locationName, Stats, uuidStr) {
  let speciesName = p.species ? String(p.species.name) : 'Unknown'
  let displayName = p.displayName ? String(p.displayName.string) : speciesName
  let level = p.level || 1
  let isShiny = Boolean(p.shiny)
  let gender = p.gender ? String(p.gender.name()) : 'GENDERLESS'
  let friendship = p.friendship || 0

  let types = []
  if (p.primaryType) types.push(String(p.primaryType.name))
  if (p.secondaryType) types.push(String(p.secondaryType.name))

  let natureName = p.nature ? String(p.nature.name.path) : 'Unknown'
  let natureInc = p.nature && p.nature.increasedStat ? String(p.nature.increasedStat.name()) : null
  let natureDec = p.nature && p.nature.decreasedStat ? String(p.nature.decreasedStat.name()) : null

  let abilityName = p.ability ? String(p.ability.name) : 'Unknown'

  let ivs = p.ivs
  let hpIV = ivs ? (ivs.get(Stats.HP) || 0) : 0
  let atkIV = ivs ? (ivs.get(Stats.ATTACK) || 0) : 0
  let defIV = ivs ? (ivs.get(Stats.DEFENCE) || 0) : 0
  let spaIV = ivs ? (ivs.get(Stats.SPECIAL_ATTACK) || 0) : 0
  let spdIV = ivs ? (ivs.get(Stats.SPECIAL_DEFENCE) || 0) : 0
  let speIV = ivs ? (ivs.get(Stats.SPEED) || 0) : 0
  let totalIV = hpIV + atkIV + defIV + spaIV + spdIV + speIV
  let ivPercent = Number(((totalIV / 186) * 100).toFixed(1))

  let evs = p.evs
  let hpEV = evs ? (evs.get(Stats.HP) || 0) : 0
  let atkEV = evs ? (evs.get(Stats.ATTACK) || 0) : 0
  let defEV = evs ? (evs.get(Stats.DEFENCE) || 0) : 0
  let spaEV = evs ? (evs.get(Stats.SPECIAL_ATTACK) || 0) : 0
  let spdEV = evs ? (evs.get(Stats.SPECIAL_DEFENCE) || 0) : 0
  let speEV = evs ? (evs.get(Stats.SPEED) || 0) : 0
  let totalEV = hpEV + atkEV + defEV + spaEV + spdEV + speEV

  let moves = []
  if (p.moveSet && p.moveSet.moves) {
    for (let m of p.moveSet.moves) {
      if (m && m.name) {
        moves.push(String(m.name))
      }
    }
  }

  let heldItem = 'None'
  try {
    let itemStack = p.heldItem()
    if (itemStack && !itemStack.isEmpty()) {
      heldItem = String(itemStack.id)
    }
  } catch (err) {}

  return {
    uuid: uuidStr,
    location: locationName,
    species: speciesName,
    display_name: displayName,
    level: level,
    shiny: isShiny,
    gender: gender,
    types: types,
    nature: natureName,
    nature_increased: natureInc,
    nature_decreased: natureDec,
    ability: abilityName,
    friendship: friendship,
    held_item: heldItem,
    ivs: {
      hp: hpIV,
      attack: atkIV,
      defence: defIV,
      special_attack: spaIV,
      special_defence: spdIV,
      speed: speIV,
      total: totalIV,
      percentage: ivPercent
    },
    evs: {
      hp: hpEV,
      attack: atkEV,
      defence: defEV,
      special_attack: spaEV,
      special_defence: spdEV,
      speed: speEV,
      total: totalEV
    },
    moves: moves
  }
}
