Sub ConvertCsvToPipeSeparated()

    Dim ws As Worksheet
    Dim outputFile As String
    Dim cell As Range
    Dim rowData As String
    Dim fileNumber As Integer
    Dim sheetName As String
    
    sheetName = "YourSheetName"

    On Error Resume Next
    Set ws = Worksheets(sheetName)
    On Error GoTo 0

    If ws Is Nothing Then
        MsgBox "Sheet named '" & sheetName & "' does not exist.", vbExclamation
        Exit Sub
    End If

    outputFile = ThisWorkbook.Path & "\" & ws.Name & "_pipe_separated.txt"
    
    fileNumber = FreeFile
    
    Open outputFile For Output As #fileNumber
    
    For Each row In ws.UsedRange.Rows
        rowData = ""
        For Each cell In row.Cells
            rowData = rowData & cell.Value & "|"
        Next cell
        Print #fileNumber, Left(rowData, Len(rowData) - 1)
    Next row

    Close #fileNumber
    
    MsgBox "Conversion complete! File saved as: " & outputFile

End Sub
