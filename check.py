const output = arr.reduce((uniqueItems, currentItem) => {
  const name = currentItem.name;
  if (!uniqueItems.some(item => item.name === name)) {
    uniqueItems.push({ name, text: name });
  }
  return uniqueItems;
}, []);
