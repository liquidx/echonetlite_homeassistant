# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Home Assistant custom component that provides integration with ECHONETLite compatible devices (primarily Japanese home appliances like air conditioners, water heaters, lighting systems, etc.). The integration uses the `pychonet` Python library to communicate with devices over the ECHONETLite protocol on port 3610.

**Important**: This repository is no longer in active development. The maintainer will respond to and approve PRs but will not actively troubleshoot issues.

## Architecture

### Core Components

- **Main Integration** (`__init__.py`): Sets up the ECHONETLite platform, manages device discovery, and handles the central ECHONETConnector
- **Config Flow** (`config_flow.py`): Handles device discovery and configuration UI
- **Platform Files**: Each Home Assistant platform has its own file (climate.py, sensor.py, switch.py, etc.)
- **Constants** (`const.py`): Large file containing EPC (ECHONETLite Property Code) mappings and device configurations
- **Quirks System**: Device-specific customizations in `quirks/` directory organized by manufacturer

### Key Architecture Patterns

1. **ECHONETConnector**: Central connector class that aggregates API calls per device instance and manages batched updates
2. **EPC Code Mapping**: Extensive mapping system in `const.py` that translates ECHONETLite property codes to Home Assistant entities
3. **Device Discovery**: Uses UDP multicast for automatic device discovery on the network
4. **Quirks System**: Allows manufacturer-specific customizations without modifying core code

### Dependencies

- **pychonet==2.6.16**: Core ECHONETLite communication library
- **Home Assistant 2024.1.0+**: Required minimum version
- **Python 3.9+**: As per GitHub workflow

## Development Commands

Based on analysis of the codebase, there are no specific build, test, or lint commands configured. The GitHub workflow is mostly commented out and only sets up Python 3.9.

## File Structure

```
custom_components/echonetlite/
├── __init__.py              # Main integration setup and ECHONETConnector
├── config_flow.py           # Device discovery and configuration
├── const.py                 # EPC mappings and device configurations  
├── manifest.json            # Integration metadata
├── services.yaml            # Service definitions
├── [platform].py           # Home Assistant platform implementations
├── quirks/                  # Device-specific customizations
│   └── [Manufacturer]/
│       └── [ProductCode]/
│           └── [DeviceClass].py
└── translations/            # UI translations
```

## Working with EPC Codes

ECHONETLite devices are identified by:
- **EOJGC**: Equipment Object Group Code (e.g., 0x01 for Air Conditioner-related)
- **EOJCC**: Equipment Object Class Code (e.g., 0x30 for Home Air Conditioner)
- **EOJCI**: Equipment Object Class Instance (device instance number)

EPC codes (Equipment Property Codes) define device properties. The `const.py` file contains extensive mappings from EPC codes to Home Assistant entity configurations.

## Device Support

The integration supports a wide range of ECHONETLite devices including:
- Mitsubishi, Sharp, Panasonic air conditioners
- Water heaters and hot water generators  
- Lighting systems
- Solar power generation systems
- Various sensors and meters
- Storage batteries and more

Each device type has specific EPC code mappings defined in `const.py`.

## Protocol Details

- Uses UDP port 3610 for ECHONETLite communication
- Supports both polling and push notifications from devices
- Implements batched updates to reduce network traffic
- Includes retry logic and timeout handling for device communication