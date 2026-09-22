// =========================================================================
// КЛИЕНТСКИЙ НАКОПИТЕЛЬНЫЙ СКАНЕР ТМ-ДИСКОВ ИЗ БОЧЕК / СУНДУКОВ
// Сканирует ID, Название, Количество И ТИП АТАКИ (Type) из тегов предмета!
// =========================================================================

let lastScanTime = 0
let globalTMSummary = {}
let scannedBarrelsCount = 0

ClientEvents.tick(event => {
  let player = Client.player
  if (!player) return

  let screen = Client.currentScreen
  let mc = Java.loadClass('net.minecraft.client.Minecraft').getInstance()
  if (!mc || !mc.getWindow()) return

  let windowHandle = mc.getWindow().getWindow()
  let GLFW = Java.loadClass('org.lwjgl.glfw.GLFW')

  let isShift = GLFW.glfwGetKey(windowHandle, 340) === 1 || GLFW.glfwGetKey(windowHandle, 344) === 1
  let isCtrl = GLFW.glfwGetKey(windowHandle, 341) === 1 || GLFW.glfwGetKey(windowHandle, 345) === 1
  let isF8 = GLFW.glfwGetKey(windowHandle, 297) === 1
  let isB = GLFW.glfwGetKey(windowHandle, 66) === 1

  let now = Date.now()
  if (now - lastScanTime < 800) return

  // 1. ОЧИСТКА БАЗЫ (Shift + F8 или Ctrl + F8)
  if ((isShift || isCtrl) && isF8) {
    lastScanTime = now
    globalTMSummary = {}
    scannedBarrelsCount = 0
    player.tell('§c[TM Scanner] 🗑 База данных очищена! Можно сканировать заново.')
    return
  }

  // 2. СКАНИРОВАНИЕ (F8 или Shift + B внутри интерфейса любого сундука/бочки)
  if (screen && screen.menu) {
    if (isF8 || (isShift && isB)) {
      lastScanTime = now
      scanAndAppendContainer(screen.menu, player)
    }
  } else if (isF8) {
    lastScanTime = now
    player.tell('§e[TM Scanner] ℹ️ Откройте бочку или сундук и нажмите F8!')
  }
})

function scanAndAppendContainer(menu, player) {
  let slots = menu.slots
  let barrelItemsFound = 0

  for (let i = 0; i < slots.length; i++) {
    let slot = slots[i]
    if (!slot) continue
    
    let stack = slot.item
    if (!stack || stack.isEmpty()) continue

    // Пропускаем слоты инвентаря игрока
    if (slot.container === player.inventory || (slot.container && slot.container.getClass().getSimpleName().includes('Inventory'))) {
      continue
    }

    let id = String(stack.id)

    // Фильтр ТМ / TR / HM дисков
    if (id.includes('simpletms') || id.includes(':tm_') || id.includes(':tr_') || id.includes(':hm_') || id.includes('tm')) {
      let name = stack.hoverName.string
      let count = stack.count

      // 🔍 Определение типа покемона из тегов предмета (#simpletms:type_ghost_tr, etc.)
      let moveType = 'normal'
      try {
        let tags = stack.tags.toArray()
        for (let tag of tags) {
          let tagStr = String(tag.location ? tag.location() : tag)
          let match = tagStr.match(/type_([a-z]+)/)
          if (match) {
            moveType = match[1]
            break
          }
        }
      } catch (err) {}

      if (!globalTMSummary[id]) {
        globalTMSummary[id] = { 
          name: name, 
          type: moveType,
          count: 0 
        }
      }
      globalTMSummary[id].count += count
      barrelItemsFound += count
    }
  }

  if (barrelItemsFound === 0) {
    player.tell('§e[TM Scanner] ⚠️ В этой бочке/сундуке не найдено ТМ-дисков!')
    return
  }

  scannedBarrelsCount++

  let sortedKeys = Object.keys(globalTMSummary).sort((a, b) => globalTMSummary[a].name.localeCompare(globalTMSummary[b].name))
  let totalAllItems = 0
  let exportList = []

  sortedKeys.forEach(id => {
    let item = globalTMSummary[id]
    totalAllItems += item.count
    exportList.push({
      id: id,
      name: item.name,
      type: item.type,
      count: item.count
    })
  })

  // Формируем структуру данных
  let exportData = {
    scanned_barrels_count: scannedBarrelsCount,
    total_unique_tms: sortedKeys.length,
    total_items_count: totalAllItems,
    tms: exportList
  }

  let filePath = 'kubejs/my_tms_inventory.json'
  try {
    JsonIO.write(filePath, exportData)

    player.tell(`§a[TM Scanner] ✔ Бочка #${scannedBarrelsCount} добавлена (+${barrelItemsFound} шт.)!`)
    player.tell(`§fВсего в базе: §e${sortedKeys.length} уникальных ТМ §f(всего: §e${totalAllItems} шт.§f)`)
    player.tell(`§bФайл сохранён в: §f${filePath}`)
    console.log(`[TM Scanner] Сохранено ${sortedKeys.length} ТМ с типами в ${filePath}`)
  } catch (e) {
    console.error(`[TM Scanner Error] ` + e)
    player.tell(`§c[TM Scanner Ошибка записи]: ` + e)
  }
}
