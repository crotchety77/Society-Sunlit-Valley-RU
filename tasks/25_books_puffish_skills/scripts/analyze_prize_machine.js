const fs = require('fs');
const path = 'D:\\ModrinthApp\\profiles\\Society_ Sunlit Valley\\kubejs\\startup_scripts\\customMachines\\prizeMachine.js';
const content = fs.readFileSync(path, 'utf8');
const startIndex = content.indexOf('global.prizeMachineRewards = [');
const endIndex = content.indexOf('StartupEvents.registry("block"', startIndex);
const rewards = new Function('global', content.substring(startIndex, endIndex) + '; return global.prizeMachineRewards;')({ global: {} });

console.log('=== ВСЕ 45 КАТЕГОРИЙ (ШАГОВ) ПРИЗОВОГО АВТОМАТА ===');
rewards.forEach((r, idx) => {
  console.log(`[Шаг ${idx.toString().padStart(2, ' ')}] "${r.hint}" -> вариантов: ${r.possibleOutputs.length} | примеры: ${r.possibleOutputs.slice(0, 2).join(', ')}`);
});
