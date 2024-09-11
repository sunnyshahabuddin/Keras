Sub ConvertCsvToPipeSeparated()

    Dim ws As Worksheet
    Dim outputFile As String
    Dim cell As Range
    Dim rowData As String
    Dim fileNumber As Integer
    
    ' Set the worksheet to the active sheet
    Set ws = ActiveSheet
    
    ' Define the output file name
    outputFile = ws.Parent.Path & "\" & ws.Name & "_pipe_separated.txt"
    
    ' Get a free file number
    fileNumber = FreeFile
    
    ' Open the output file for writing
    Open outputFile For Output As #fileNumber
    
    ' Loop through each row in the sheet
    For Each row In ws.UsedRange.Rows
        rowData = ""
        ' Loop through each cell in the row
        For Each cell In row.Cells
            ' Append cell value to row data separated by '|'
            rowData = rowData & cell.Value & "|"
        Next cell
        ' Remove the trailing '|' and write to the output file
        Print #fileNumber, Left(rowData, Len(rowData) - 1)
    Next row

    ' Close the output file
    Close #fileNumber
    
    MsgBox "Conversion complete! File saved as: " & outputFile

End Sub
