const { performance } = require('perf_hooks');
const fs = require('fs');

function insert(tree, gene, ind, health) {
  for (const c of gene) {
    tree[c] = tree[c] ?? {};
    tree = tree[c];
  }
  tree.data = tree.data ?? [];
  tree.data.push([ind, health]);
}

function init(genes, health) {
  const tree = {};
  for (let i = 0; i < genes.length; i++) {
    insert(tree, genes[i], i, health[i]);
  }
  return tree;
}

function bSearch(data, ind) {
  let ret = 0;
  let i = 0;
  let j = data.length - 1;
  while (i <= j) {
    const mid = (i + j) >> 1;

    if (ind > data[mid][0]) {
      i = mid + 1;
      ret = i;
    } else {
      j = mid - 1;
      ret = mid;
    }
  }

  return ret;
}

// function getSubStrHealth(tree, first, last, d, i) {
//   let h = 0;
//   while (tree) {
//     tree = tree[d[i]];
//     const data = tree?.data ?? [];
//
//     let j = bSearch(data, first);
//     while (j < data.length && data[j][0] <= last) {
//       h += data[j][1];
//       j++;
//     }
//
//     i++;
//   }
//   return h;
// }

function getSubStrHealth(tree, first, last, d, i) {
  let h = 0;
  while (tree) {
    tree = tree[d[i]];
    const data = tree?.data ?? [];

    for (let j = 0; j < data.length; j++) {
      if (data[j][0] >= first && data[j][0] <= last) {
        h += data[j][1];
      }
    }

    i++;
  }
  return h;
}

function getHealth(tree, first, last, d) {
  let h = 0;
  for (let i = 0; i < d.length; i++) {
    h += getSubStrHealth(tree, first, last, d, i);
  }
  return h;
}

function main() {
  const lines = fs.readFileSync('input.txt', 'utf-8').split(/\r?\n/);
  const n = lines[0];

  const genes = lines[1].split(' ');
  const health = lines[2].split(' ').map(x => parseInt(x));
  const tree = init(genes, health);
  const s = parseInt(lines[3].trim(), 10);

  const r = [];
  for (let sItr = 0; sItr < s; sItr++) {
    const firstMultipleInput = lines[sItr + 4].replace(/\s+$/g, '').split(' ');

    const first = parseInt(firstMultipleInput[0], 10);
    const last = parseInt(firstMultipleInput[1], 10);

    const d = firstMultipleInput[2];
    const h = getHealth(tree, first, last, d);
    // console.log(h);
    r.push(h);
  }
  console.log(Math.min(...r), Math.max(...r));
}

const startTime = performance.now();
main();
const endTime = performance.now();
console.log(`time  ${(endTime - startTime) / 1000} milliseconds`);
