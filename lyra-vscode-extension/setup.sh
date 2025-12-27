#!/bin/bash
# Lyra VS Code Extension Quick Setup

echo "🦈 Lyra Language Support - Setup Script"
echo "========================================"
echo ""

# Step 1: Install dependencies
echo "📦 Installing dependencies..."
npm install

# Step 2: Build
echo "🔨 Building extension..."
npm run build

# Step 3: Package
echo "📦 Packaging extension..."
vsce package

echo ""
echo "✅ Done!"
echo ""
echo "Next steps:"
echo "1. Replace icon.png with your shark logo"
echo "2. Run: vsce create-publisher lyra-dev"
echo "3. Run: vsce publish -p [YOUR_PAT_TOKEN]"
echo ""
echo "Or test locally:"
echo "- VS Code → Extensions → Install from VSIX"
echo "- Select the generated .vsix file"
