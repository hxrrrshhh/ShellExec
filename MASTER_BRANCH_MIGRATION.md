# Master Branch Migration Guide

This document provides instructions for completing the migration from 'main' to 'master' as the default branch for the ShellExec repository.

## What Has Been Completed

✅ **File-based References Updated**
- All documentation now references `master` as the default branch
- GitHub Actions workflows configured for `master` branch
- Contributing guidelines updated for `master` branch workflow
- Issue and PR templates reference `master` branch
- README.md updated with comprehensive documentation

✅ **Repository Configuration Files Added**
- `.gitignore` - Python project gitignore
- `requirements.txt` - Python dependencies
- `.github/workflows/ci.yml` - CI/CD pipeline for master branch
- `CONTRIBUTING.md` - Contribution guidelines
- Issue and PR templates

## Remaining Manual Steps (Repository Administrator Required)

### 1. Change Default Branch in GitHub Settings

**Important:** This step must be completed by a repository administrator through the GitHub web interface.

1. Go to the repository settings: https://github.com/hxrrrshhh/ShellExec/settings
2. Click on "Branches" in the left sidebar
3. Under "Default branch", click the switch/edit button
4. Select `master` as the new default branch
5. Click "Update" and confirm the change

### 2. Update Branch Protection Rules

1. In repository settings → Branches
2. If there are existing branch protection rules for `main`:
   - Copy the rules to apply them to `master`
   - Remove protection rules from `main` if desired
3. Ensure `master` branch has appropriate protection rules:
   - Require pull request reviews before merging
   - Require status checks to pass before merging
   - Require branches to be up to date before merging
   - Include administrators in restrictions (if desired)

### 3. Update Deployment Settings

If there are any deployment configurations:
1. Update deployment settings to deploy from `master` branch
2. Update any webhooks or integrations that reference the default branch
3. Check any external CI/CD systems (if applicable) and update them to track `master`

### 4. Clean Up (Optional)

After confirming everything works with `master` as default:
1. The `main` branch can be deleted if it's no longer needed
2. Update any external documentation or wikis that reference `main`
3. Notify team members about the branch change

## Verification Steps

After completing the manual steps:

1. ✅ Verify new repositories clone `master` branch by default
2. ✅ Verify pull requests target `master` branch by default
3. ✅ Verify CI/CD workflows trigger on `master` branch
4. ✅ Verify branch protection rules are active on `master`
5. ✅ Test that deployment processes work with `master` branch

## For Contributors

Once the default branch change is complete:

```bash
# For existing contributors with local clones
git fetch origin
git branch -m main master 2>/dev/null || true  # Rename local main if it exists
git branch -u origin/master master
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/master

# For new contributors
git clone https://github.com/hxrrrshhh/ShellExec.git
cd ShellExec
# Will automatically checkout master branch
```

## Summary

All file-based configurations have been updated to reference `master` as the default branch. The only remaining step is to change the GitHub repository settings to make `master` the actual default branch, which requires repository administrator access.