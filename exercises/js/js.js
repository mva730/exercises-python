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

function getSubStrHealth(tree, first, last, d, i) {
  let h = 0;
  while (tree) {
    tree = tree[d[i]];
    const data = tree?.data ?? [];

    let j = bSearch(data, first);
    while (j < data.length && data[j][0] <= last) {
      h += data[j][1];
      j++;
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

let genes = 'a b c aa d b'.split(' ')
let health = '1 2 3 4 5 6'.split(' ').map(x => parseInt(x))

const tree = init(genes, health);

// const s = parseInt(readLine().trim(), 10);
let min = Infinity;
let max = 0;
// for (let sItr = 0; sItr < s; sItr++) {
  // const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

  // const first = parseInt(firstMultipleInput[0], 10);
  //
  // const last = parseInt(firstMultipleInput[1], 10);
  //
  // const d = firstMultipleInput[2];

  first = 1
  last = 5
  d = 'caaab'
  const h = getHealth(tree, first, last, d);

  min = Math.min(min, h);
  max = Math.max(max, h);
// }
console.log(`${min} ${max}`);