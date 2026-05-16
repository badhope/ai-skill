# Git Synchronization Guide

This guide explains how to keep your local repository in sync with the remote, ensuring main branch always stays up to date.

## Prerequisites

1. Have git installed
2. Have your GitHub token ready
3. Be on the main branch (or the branch you want to sync)

## Basic Workflow

### 1. Check Current Status

```bash
git status
```

### 2. Pull Latest Changes

```bash
git pull origin main
```

### 3. Add and Commit Local Changes

```bash
git add .
git commit -m "Your meaningful commit message"
```

### 4. Push to Remote

```bash
git push origin main
```

## Advanced: If You Have Conflicts

### 1. Pull with Rebase

```bash
git pull --rebase origin main
```

### 2. Resolve Conflicts (if any)

Edit the conflicting files, then:

```bash
git add <resolved-file>
git rebase --continue
```

### 3. Push After Rebase

```bash
git push origin main --force-with-lease
```

## Quick Sync Script

Create a `sync.sh` file:

```bash
#!/bin/bash
# Quick sync script for AI-SKILL

echo "🔄 Syncing with remote..."

# Check status
git status

# Pull latest
echo "📥 Pulling latest changes..."
git pull origin main

# Add all changes
echo "📤 Adding local changes..."
git add .

# Commit if changes
if git diff --staged --quiet; then
    echo "✅ No changes to commit"
else
    echo "📝 Committing changes..."
    read -p "Enter commit message: " commit_msg
    git commit -m "${commit_msg:-Update AI-SKILL}"
    
    echo "🚀 Pushing to remote..."
    git push origin main
fi

echo "✨ Sync complete!"
```

Make it executable:
```bash
chmod +x sync.sh
```

Run:
```bash
./sync.sh
```

## Best Practices

1. **Always pull before you push** - Get latest changes first
2. **Meaningful commit messages** - Describe what you changed
3. **Commit often** - Don't wait for huge changes
4. **Small atomic commits** - One logical change per commit
5. **Push after each change** - Keep remote in sync

## GitHub Token Setup

If you need to set your token:

```bash
git remote set-url origin https://<your-token>@github.com/badhope/AI-SKILL.git
```

Or use Git credential helper:
```bash
git config --global credential.helper store
```

## Troubleshooting

### "Your branch is behind..."

```bash
git pull origin main
```

### "Your branch and origin have diverged..."

```bash
git fetch origin
git reset --hard origin/main  # WARNING: Loses local changes!
# OR
git pull --rebase origin main
```

### Permission Denied

Make sure your token has push access to the repository.
