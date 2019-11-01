import { link } from "fs";

/**
 * 将二维数组导出为 csv
 * @param {Array<Array<any>>} rows
 */
function exportCSV(rows, headers = undefined, filename = "my_csv") {
  console.group("CSV");
  console.log(rows);
  let csvContent = "data:text/csv;charset=utf-8,";

  if (headers) {
    csvContent +=
      headers.join(",") + "\n" + rows.map(e => e.join(",")).join("\n");
  } else {
    csvContent += rows.map(e => e.join(",")).join("\n");
  }
  console.log(csvContent);
  let encodedUri = encodeURI(csvContent);
  let _a = document.createElement("a");
  _a.setAttribute("href", encodedUri);
  _a.setAttribute("download", `${filename}.csv`);
  _a.click();
  console.log(encodedUri);
  //   window.open(encodedUri);
  console.groupEnd();
}

export { exportCSV };
