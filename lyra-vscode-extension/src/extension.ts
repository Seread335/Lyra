import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  console.log('Lyra Language Support is now active!');

  // Command: Run Lyra file
  let runFile = vscode.commands.registerCommand('lyra.runFile', () => {
    const editor = vscode.window.activeTextEditor;
    
    if (!editor) {
      vscode.window.showErrorMessage('No file is currently open');
      return;
    }

    const filePath = editor.document.fileName;
    
    // Check if file is Lyra
    if (!filePath.endsWith('.lyra')) {
      vscode.window.showWarningMessage('This is not a Lyra file (.lyra)');
      return;
    }

    // Create or show terminal
    const terminal = vscode.window.createTerminal('Lyra');
    terminal.show();
    
    // Run the file
    terminal.sendText(`lyra "${filePath}"`);
    
    vscode.window.showInformationMessage(`Running ${editor.document.fileName}...`);
  });

  context.subscriptions.push(runFile);
}

export function deactivate() {
  console.log('Lyra Language Support deactivated');
}
