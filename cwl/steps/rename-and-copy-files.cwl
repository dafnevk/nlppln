#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.rename-and-copy-files"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 3

inputs:
- id: in_dir
  type: Directory
  inputBinding:
    position: 2

outputs:
- id: out_files
  type:
    type: array
    items: File
  outputBinding:
    glob: "*"
