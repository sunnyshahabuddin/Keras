import React from 'react';
import XLSX from 'xlsx';

const DownloadButton = ({ data, fileName }) => {
  const downloadExcel = () => {
    // Create a new workbook and add a worksheet
    const workbook = XLSX.utils.book_new();
    const worksheet = XLSX.utils.json_to_sheet(data);

    // Add the worksheet to the workbook
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');

    // Create a Blob containing the workbook data
    const blob = XLSX.write(workbook, { bookType: 'xlsx', type: 'blob' });

    // Create a download link and trigger a click event to download the file
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName || 'data.xlsx';
    a.click();

    // Clean up
    window.URL.revokeObjectURL(url);
  };

  return (
    <button onClick={downloadExcel}>
      Download Excel
    </button>
  );
};

export default DownloadButton;
