console.info("[SOCIETY] handleDebt.js loaded");

CommonAddedEvents.playerRespawn((e) => {
  const { player, server } = e;
  if (global.enableDeathDebt) {
    const UUID = player.getUuid().toString();
    if (!server.persistentData.hospitalVisits) server.persistentData.hospitalVisits = {};
    server.persistentData.hospitalVisits[UUID] = (server.persistentData.hospitalVisits[UUID] || 0) + 1;
    let visits = server.persistentData.hospitalVisits[UUID];

    if (!player.stages.has("first_death")) {
      player.stages.add("first_death");
      let quoteKey = global.getHospitalQuoteKey(visits);
      let noteText = Text.translatable("society.hospital_receipt.note.free", `${visits}`, Text.translatable(quoteKey)).toJson();
      let noteTitle = `Больничная справка #${visits}`;
      let noteAuthor = global.translatableWithFallback("society.hospital_receipt.author", "Doctor Harvey").getString();
      player.give(
        global.getNotePaperItem(noteAuthor, noteText, noteTitle)
      );
      server.runCommandSilent(
        global.getEmbersTextAPICommand(
          player.username,
          `{anchor:"TOP_LEFT",background:1,color:"#55FF55",size:1,offsetY:36,offsetX:6,typewriter:1,align:"TOP_LEFT"}`,
          220,
          Text.translatable("society.hospital_receipt.hud.first_death").toJson()
        )
      );
      player.tell(Text.translatable("society.hospital_receipt.hud.first_death").green());
      player.tell(Text.translatable(quoteKey).italic().gray());
    } else {
      global.handleFee(server, player, "death");
      if (!player.stages.has("first_aid_guide") && Math.random() <= 0.01)
        player.give("society:first_aid_guide");
    }
    player.potionEffects.add("minecraft:slowness", 1200, 0, false, true);
  }
});
