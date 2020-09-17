//-------------Form related functions----------------

function exportDisplayForm(data, displayAttributes){
  let result = [];
  for(let item of data){
    for(let key in item){if (item[key] === 'nan'){item[key] = ''}}
    let entry = [];
    for (let attribute of displayAttributes){
      entry.push(item[attribute])
    }
    result.push(entry)
  }
  return result
}

export {exportDisplayForm}