#!/usr/bin/env python3
"""
Test script to verify the datasource mapping fix in run_group_voxelWise.py
"""

def test_datasource_mapping():
    """Test that datasource mapping works correctly"""
    print("Testing datasource mapping...")
    
    # This is the DATA_SOURCE_CONFIGS from run_group_voxelWise.py
    DATA_SOURCE_CONFIGS = {
        'standard': {
            'description': 'Standard group-level analysis',
            'requires_varcope': True,
            'requires_grp': True,
            'results_subdir': 'groupLevel_timeEffect/whole_brain',
            'workflows_subdir': 'whole_brain',
            'script_name': 'run_group_voxelWise.py'
        },
        'placebo': {
            'description': 'Placebo-specific group-level analysis',
            'requires_varcope': True,
            'requires_grp': True,
            'results_subdir': 'groupLevel_timeEffect/whole_brain/Placebo',
            'workflows_subdir': 'whole_brain/Placebo',
            'script_name': 'run_group_voxelWise.py'
        },
        'guess': {
            'description': 'Guess-specific group-level analysis',
            'requires_varcope': True,
            'requires_grp': True,
            'results_subdir': 'groupLevel_timeEffect/whole_brain/Guess',
            'workflows_subdir': 'whole_brain/Guess',
            'script_name': 'run_group_voxelWise.py'
        }
    }
    
    # Test the path construction logic
    SCRUBBED_DIR = '/scrubbed_dir'
    PROJECT_NAME = 'NARSAD'
    
    def get_standard_paths(task, contrast, base_dir, data_source):
        """Mock function to test path construction"""
        data_source_config = DATA_SOURCE_CONFIGS.get(data_source, DATA_SOURCE_CONFIGS['standard'])
        
        # Set up directories
        results_dir = os.path.join(base_dir, data_source_config['results_subdir'])
        # workflows_subdir now contains 'whole_brain[/Placebo]', so we add 'groupLevel_timeEffect' here
        workflows_dir = os.path.join(SCRUBBED_DIR, PROJECT_NAME, 'work_flows', 'groupLevel_timeEffect', data_source_config['workflows_subdir'])
        
        # Define paths
        result_dir = os.path.join(results_dir, f'task-{task}', f'cope{contrast}')
        workflow_dir = os.path.join(workflows_dir, f'task-{task}', f'cope{contrast}')
        
        return {
            'result_dir': result_dir,
            'workflow_dir': workflow_dir
        }, data_source_config
    
    # Test standard datasource
    print("\n1. Testing 'standard' datasource:")
    try:
        paths, config = get_standard_paths('phase2', 28, '/data/NARSAD/MRI/derivatives/fMRI_analysis', 'standard')
        print(f"   Results dir: {paths['result_dir']}")
        print(f"   Workflow dir: {paths['workflow_dir']}")
        print(f"   Config description: {config['description']}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test placebo datasource
    print("\n2. Testing 'placebo' datasource:")
    try:
        paths, config = get_standard_paths('phase2', 28, '/data/NARSAD/MRI/derivatives/fMRI_analysis', 'placebo')
        print(f"   Results dir: {paths['result_dir']}")
        print(f"   Workflow dir: {paths['workflow_dir']}")
        print(f"   Config description: {config['description']}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test guess datasource
    print("\n3. Testing 'guess' datasource:")
    try:
        paths, config = get_standard_paths('phase2', 28, '/data/NARSAD/MRI/derivatives/fMRI_analysis', 'guess')
        print(f"   Results dir: {paths['result_dir']}")
        print(f"   Workflow dir: {paths['workflow_dir']}")
        print(f"   Config description: {config['description']}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test invalid datasource (should fall back to standard)
    print("\n4. Testing invalid datasource (should fall back to standard):")
    try:
        paths, config = get_standard_paths('phase2', 28, '/data/NARSAD/MRI/derivatives/fMRI_analysis', 'invalid')
        print(f"   Results dir: {paths['result_dir']}")
        print(f"   Workflow dir: {paths['workflow_dir']}")
        print(f"   Config description: {config['description']}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Show the actual DATA_SOURCE_CONFIGS
    print("\n5. Current DATA_SOURCE_CONFIGS:")
    for key, config in DATA_SOURCE_CONFIGS.items():
        print(f"   '{key}': {config['description']}")
        print(f"     results_subdir: {config['results_subdir']}")
        print(f"     workflows_subdir: {config['workflows_subdir']}")

if __name__ == "__main__":
    import os
    test_datasource_mapping()
