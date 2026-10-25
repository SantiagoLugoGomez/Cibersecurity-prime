#!/usr/bin/env bash
# Take a VirtualBox snapshot of every VM whose name starts with a prefix.
# Usage: ./snapshot-all.sh lab- "before-stage-3"
set -euo pipefail

prefix="${1:?usage: $0 <vm-name-prefix> <snapshot-name>}"
snapshot="${2:?usage: $0 <vm-name-prefix> <snapshot-name>}"

VBoxManage list vms | sed -n 's/^"\(.*\)" {.*}$/\1/p' | while read -r vm; do
    case "$vm" in
        "$prefix"*)
            echo "Snapshotting $vm"
            VBoxManage snapshot "$vm" take "$snapshot"
            ;;
    esac
done
