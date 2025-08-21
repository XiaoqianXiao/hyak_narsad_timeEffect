# NARSAD fMRI Analysis Pipeline - Deployment Checklist

## ✅ Local Validation Results

All local tests have passed successfully! The pipeline is ready for deployment to the supercomputer.

### Test Results Summary
- **File Structure**: ✓ PASS - All required files present
- **Python Syntax**: ✓ PASS - All Python files have valid syntax
- **Condition Naming Consistency**: ✓ PASS - CS-_first_half naming consistent across files
- **Container Path Consistency**: ✓ PASS - Container paths correctly configured
- **Behavioral Data Access**: ✓ PASS - Behavioral data files accessible and correctly formatted
- **Utility Functions**: ✓ PASS - CSV reading and condition parsing working correctly

## 🔍 Behavioral Data Structure Verified

The behavioral data files have the expected structure:
- **Phase 2**: 63 trials, 4 CS-_first_half trials (onsets: 12, 107, 147, 166)
- **Phase 3**: 52 trials, 4 CS-_first_half trials (onsets: 40, 154, 230, 289)

Condition splitting logic will correctly create:
- `CS-_first_half_first` (first trial)
- `CS-_first_half_others` (remaining trials)

## 🚀 Deployment Steps

### 1. Upload Code to Supercomputer
```bash
# Upload all files to the supercomputer
scp -r . username@supercomputer:/path/to/destination/
```

### 2. Build Container
```bash
# On the supercomputer, build the container
sudo apptainer build narsad-fmri_timeEffect_1.0.sif run_1st_level.def
```

### 3. Verify Container Build
```bash
# Check that container was created successfully
ls -la narsad-fmri_timeEffect_1.0.sif
```

### 4. Generate SLURM Scripts
```bash
# Generate SLURM scripts for all subjects
python3 create_1st_voxelWise.py
```

### 5. Launch Jobs
```bash
# Launch all jobs
./launch_1st_voxelWise.sh

# Or launch specific phases
./launch_1st_voxelWise.sh --phase phase2
./launch_1st_voxelWise.sh --phase phase3

# Dry run to see what would be launched
./launch_1st_voxelWise.sh --dry-run
```

## 📁 File Structure

```
hyak_narsad_timeEffect/
├── create_1st_voxelWise.py      # Main script for generating SLURM jobs
├── first_level_workflows.py     # Nipype workflow definitions
├── utils.py                     # Utility functions for data processing
├── launch_1st_voxelWise.sh     # SLURM job launcher
├── run_1st_level.def           # Container definition file
└── DEPLOYMENT_CHECKLIST.md      # This file
```

## 🔧 Configuration Details

### Container Path
- **Container**: `narsad-fmri_timeEffect_1.0.sif`
- **Base Image**: `narsad-fmri_timeEffect_0.0.sif` (referenced in .def file)

### Working Directories
- **First Level Scripts**: `/gscratch/scrubbed/fanglab/xiaoqian/NARSAD/work_flows/firstLevel_timeEffect`
- **First Level Output**: `/gscratch/fanglab/xiaoqian/NARSAD/MRI/derivatives/fMRI_analysis/firstLevel_timeEffect`
- **Group Level Scripts**: `/gscratch/scrubbed/fanglab/xiaoqian/NARSAD/work_flows/groupLevel_timeEffect`
- **Group Level Output**: `/gscratch/fanglab/xiaoqian/NARSAD/MRI/derivatives/fMRI_analysis/groupLevel_timeEffect`
- **Output**: `/gscratch/fanglab/xiaoqian/NARSAD/MRI/derivatives/fMRI_analysis`

### SLURM Configuration
- **Account**: fang
- **Partition**: ckpt-all
- **Resources**: 1 node, 1 task, 4 CPUs, 40GB RAM, 2 hours

## ⚠️ Important Notes

1. **Container Dependencies**: Ensure the base image `narsad-fmri_timeEffect_0.0.sif` exists before building
2. **File Permissions**: The launcher script will automatically make SLURM scripts executable
3. **Path Consistency**: All paths are now correctly aligned between script generation and launching
4. **Condition Handling**: CS-_first_half trials are automatically split into first trial and others for proper analysis
5. **Repository Paths**: All scripts now correctly mount from `hyak_narsad_timeEffect` instead of `hyak_narsad` - this was critical for resolving the condition naming mismatch

## 🧪 Testing Commands

### Local Testing (Already Completed)
```bash
python3 test_local_validation.py
python3 test_condition_parsing.py
```

### Supercomputer Testing
```bash
# Test container build
sudo apptainer build narsad-fmri_timeEffect_1.0.sif run_1st_level.def

# Test script generation (dry run)
python3 create_1st_voxelWise.py --help

# Test launcher (dry run)
./launch_1st_voxelWise.sh --dry-run
```

## 📊 Expected Output

After successful execution, you should see:
- SLURM scripts generated in `{SCRIPTS_BASE_DIR}/{phase}/` directories
- Job submission messages for each subject/task combination
- Output files in the specified output directory structure

## 🆘 Troubleshooting

If issues arise:
1. Check container build logs
2. Verify file paths exist on supercomputer
3. Check SLURM job status with `squeue`
4. Review job output/error files in working directories

---

**Status**: ✅ READY FOR DEPLOYMENT  
**Last Updated**: $(date)  
**Tested By**: Local validation script
