---
id: webgpu-claude-skill-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:46.149269
---

# KNOWLEDGE EXTRACT: webgpu-claude-skill
> **Extracted on:** 2026-03-30 13:14:20
> **Source:** webgpu-claude-skill

---

## File: `README.md`
```markdown
# WebGPU Three.js TSL Skill

An Agent Skill for developing WebGPU-enabled Three.js applications using TSL (Three.js Shading Language).

## Overview

This skill provides Claude with comprehensive knowledge for:

- Setting up Three.js with WebGPU renderer
- Writing shaders using TSL (Three.js Shading Language)
- Creating node-based materials
- Building GPU compute shaders
- Implementing post-processing effects
- Integrating custom WGSL code

## Installation

### Claude Code

```bash
# Install from this repository
/skill install webgpu-threejs-tsl@<your-github-username>/webgpu-claude-skill
```

### Manual Installation

Copy the `skills/webgpu-threejs-tsl` folder to:
- **Global**: `~/.claude/skills/`
- **Project**: `<project>/.claude/skills/`

## Skill Structure

```
skills/webgpu-threejs-tsl/
├── SKILL.md                    # Entry point with overview
├── REFERENCE.md                # Quick reference cheatsheet
├── docs/
│   ├── core-concepts.md        # Types, operators, uniforms, control flow
│   ├── materials.md            # Node materials and properties
│   ├── compute-shaders.md      # GPU compute documentation
│   ├── post-processing.md      # Built-in and custom effects
│   ├── wgsl-integration.md     # Custom WGSL functions
│   └── device-loss.md          # GPU device loss handling and recovery
├── examples/
│   ├── basic-setup.js          # Minimal WebGPU project
│   ├── custom-material.js      # Custom shader material
│   ├── particle-system.js      # GPU compute particles
│   ├── post-processing.js      # Effect pipeline
│   └── earth-shader.js         # Complete Earth with atmosphere
└── templates/
    ├── webgpu-project.js       # Starter project template
    └── compute-shader.js       # Compute shader template
```

## Topics Covered

### Core Concepts
- Types and constructors (float, vec2, vec3, vec4, color, uniform)
- Vector swizzling
- Operators and math functions
- Control flow (If, Loop, Fn)
- Time and animation

### Materials
- All node material types
- Material properties (color, roughness, metalness, etc.)
- Physical material features (clearcoat, transmission, iridescence)
- Vertex displacement

### Compute Shaders
- Instanced array buffers
- Parallel physics simulation
- Particle systems
- Atomic operations and barriers

### Post-Processing
- Built-in effects (bloom, blur, FXAA, DOF)
- Custom effects with Fn()
- Effect chaining
- Multiple render targets

### WGSL Integration
- Custom WGSL functions with wgslFn()
- Hybrid TSL/WGSL approaches
- Performance optimization

### Device Loss Handling
- Detecting GPU device loss
- Recovery strategies
- Testing with destroy() and Chrome GPU crash
- State preservation and restoration

## Quick Example

```javascript
import * as THREE from 'three/webgpu';
import { color, time, oscSine, normalWorld, cameraPosition, positionWorld, Fn, float } from 'three/tsl';

// WebGPU renderer
const renderer = new THREE.WebGPURenderer();
await renderer.init();

// TSL material with animated fresnel
const material = new THREE.MeshStandardNodeMaterial();

material.colorNode = color(0x0066ff);

material.emissiveNode = Fn(() => {
  const viewDir = cameraPosition.sub(positionWorld).normalize();
  const fresnel = float(1).sub(normalWorld.dot(viewDir).saturate()).pow(3);
  return color(0x00ffff).mul(fresnel).mul(oscSine(time));
})();
```

## Compatibility

- **Recommended Three.js version**: r171+
- **Target browsers**: Chrome 113+, Edge 113+, Firefox (behind flag), Safari (WebGPU preview)

### Version Notes

- **r178+**: `PI2` deprecated (use `TWO_PI`), `transformedNormalView/World` renamed to `normalView/World`
- **r171+**: Stable TSL API, requires `three/webgpu` import map entry

## Resources

- [Three.js TSL Documentation](https://threejs.org/docs/pages/TSL.html)
- [Three.js Shading Language Wiki](https://github.com/mrdoob/three.js/wiki/Three.js-Shading-Language)
- [Three.js WebGPU Examples](https://github.com/mrdoob/three.js/tree/master/examples)
- [WebGPU Best Practices](https://toji.dev/webgpu-best-practices/)
- [Agent Skills Specification](https://github.com/anthropics/skills)

## License

MIT License

Code examples derived from [Three.js](https://github.com/mrdoob/three.js) (MIT License).
```

## File: `skills/webgpu-threejs-tsl/REFERENCE.md`
```markdown
# TSL Quick Reference

## Imports

```javascript
// WebGPU Three.js
import * as THREE from 'three/webgpu';

// Core TSL
import {
  float, int, uint, bool,
  vec2, vec3, vec4, color,
  mat2, mat3, mat4,
  uniform, texture, uv,
  Fn, If, Loop, Break, Continue,
  time, deltaTime
} from 'three/tsl';
```

## Types

| TSL | WGSL | Example |
|-----|------|---------|
| `float(1.0)` | `f32` | Scalar float |
| `int(1)` | `i32` | Signed integer |
| `uint(1)` | `u32` | Unsigned integer |
| `bool(true)` | `bool` | Boolean |
| `vec2(x, y)` | `vec2<f32>` | 2D vector |
| `vec3(x, y, z)` | `vec3<f32>` | 3D vector |
| `vec4(x, y, z, w)` | `vec4<f32>` | 4D vector |
| `color(0xff0000)` | `vec3<f32>` | RGB color |
| `uniform(value)` | uniform | Dynamic value |

## Operators

| Operation | TSL | GLSL Equivalent |
|-----------|-----|-----------------|
| Add | `a.add(b)` | `a + b` |
| Subtract | `a.sub(b)` | `a - b` |
| Multiply | `a.mul(b)` | `a * b` |
| Divide | `a.div(b)` | `a / b` |
| Modulo | `a.mod(b)` | `mod(a, b)` |
| Negate | `a.negate()` | `-a` |
| Less Than | `a.lessThan(b)` | `a < b` |
| Greater Than | `a.greaterThan(b)` | `a > b` |
| Equal | `a.equal(b)` | `a == b` |
| And | `a.and(b)` | `a && b` |
| Or | `a.or(b)` | `a \|\| b` |
| Assign | `a.assign(b)` | `a = b` |
| Add Assign | `a.addAssign(b)` | `a += b` |

## Swizzling

```javascript
const v = vec3(1, 2, 3);
v.x        // 1
v.xy       // vec2(1, 2)
v.zyx      // vec3(3, 2, 1)
v.rgb      // same as xyz
```

## Math Functions

| Function | Description |
|----------|-------------|
| `abs(x)` | Absolute value |
| `sign(x)` | Sign (-1, 0, 1) |
| `floor(x)` | Round down |
| `ceil(x)` | Round up |
| `fract(x)` | Fractional part |
| `min(a, b)` | Minimum |
| `max(a, b)` | Maximum |
| `clamp(x, lo, hi)` | Clamp to range |
| `mix(a, b, t)` | Linear interpolation |
| `step(edge, x)` | Step function |
| `smoothstep(a, b, x)` | Smooth step |
| `sin(x)`, `cos(x)` | Trigonometry |
| `pow(x, y)` | Power |
| `sqrt(x)` | Square root |
| `length(v)` | Vector length |
| `distance(a, b)` | Distance |
| `dot(a, b)` | Dot product |
| `cross(a, b)` | Cross product |
| `normalize(v)` | Unit vector |
| `reflect(i, n)` | Reflection |

## Geometry Nodes

| Node | Description |
|------|-------------|
| `positionLocal` | Model space position |
| `positionWorld` | World space position |
| `positionView` | Camera space position |
| `normalLocal` | Model space normal |
| `normalWorld` | World space normal |
| `normalView` | Camera space normal |
| `uv()` | UV coordinates |
| `uv(1)` | Secondary UVs |
| `tangentLocal` | Tangent vector |
| `vertexColor()` | Vertex colors |

## Camera Nodes

| Node | Description |
|------|-------------|
| `cameraPosition` | Camera world position |
| `cameraNear` | Near plane |
| `cameraFar` | Far plane |
| `cameraViewMatrix` | View matrix |
| `cameraProjectionMatrix` | Projection matrix |
| `screenUV` | Screen UV (0-1) |
| `screenSize` | Screen dimensions |

## Time

| Node | Description |
|------|-------------|
| `time` | Seconds since start |
| `deltaTime` | Frame delta |
| `oscSine(t)` | Sine wave (0-1) |
| `oscSquare(t)` | Square wave |
| `oscTriangle(t)` | Triangle wave |
| `oscSawtooth(t)` | Sawtooth wave |

## Material Properties

```javascript
const mat = new THREE.MeshStandardNodeMaterial();

// Basic
mat.colorNode = color(0xff0000);
mat.opacityNode = float(0.8);
mat.alphaTestNode = float(0.5);

// PBR
mat.roughnessNode = float(0.5);
mat.metalnessNode = float(0.0);
mat.emissiveNode = color(0x000000);
mat.normalNode = normalMap(tex);

// Physical (MeshPhysicalNodeMaterial)
mat.clearcoatNode = float(1.0);
mat.transmissionNode = float(0.9);
mat.iridescenceNode = float(1.0);
mat.sheenNode = float(1.0);

// Vertex
mat.positionNode = displaced;
```

## Control Flow

```javascript
// If-Else
If(condition, () => {
  // true
}).ElseIf(other, () => {
  // other true
}).Else(() => {
  // false
});

// Select (ternary)
const result = select(condition, trueVal, falseVal);

// Loop
Loop(10, ({ i }) => {
  // i = 0 to 9
});

// Loop control
Break();
Continue();
Discard();  // Fragment only
```

## Custom Functions

```javascript
// Basic function
const myFn = Fn(([a, b]) => {
  return a.add(b);
});

// With defaults
const myFn = Fn(([a = 1.0, b = 2.0]) => {
  return a.add(b);
});

// Usage
myFn(x, y);
myFn();  // uses defaults
```

## Compute Shaders

```javascript
// Storage buffers
const positions = instancedArray(count, 'vec3');
const values = instancedArray(count, 'float');

// Compute shader
const compute = Fn(() => {
  const pos = positions.element(instanceIndex);
  pos.addAssign(vec3(0.01, 0, 0));
})().compute(count);

// Execute
await renderer.computeAsync(compute);  // Once
renderer.compute(compute);              // Each frame
```

## Post-Processing

```javascript
import { pass } from 'three/tsl';
import { bloom } from 'three/addons/tsl/display/BloomNode.js';

// Setup
const postProcessing = new THREE.PostProcessing(renderer);
const scenePass = pass(scene, camera);
const color = scenePass.getTextureNode('output');

// Apply effects
const bloomPass = bloom(color);
postProcessing.outputNode = color.add(bloomPass);

// Render
postProcessing.render();
```

## Common Patterns

### Fresnel

```javascript
const viewDir = cameraPosition.sub(positionWorld).normalize();
const fresnel = float(1).sub(normalWorld.dot(viewDir).saturate()).pow(3);
```

### Animated UV

```javascript
const animUV = uv().add(vec2(time.mul(0.1), 0));
```

### Noise Hash

```javascript
const noise = fract(position.dot(vec3(12.9898, 78.233, 45.543)).sin().mul(43758.5453));
```

### Dissolve

```javascript
const noise = hash(positionLocal.mul(50));
If(noise.lessThan(threshold), () => Discard());
```

### Color Gradient

```javascript
const gradient = mix(colorA, colorB, positionLocal.y.mul(0.5).add(0.5));
```

## Node Materials

| Material | Use Case |
|----------|----------|
| `MeshBasicNodeMaterial` | Unlit |
| `MeshStandardNodeMaterial` | PBR |
| `MeshPhysicalNodeMaterial` | Advanced PBR |
| `MeshPhongNodeMaterial` | Phong shading |
| `MeshToonNodeMaterial` | Cel shading |
| `PointsNodeMaterial` | Point clouds |
| `LineBasicNodeMaterial` | Lines |
| `SpriteNodeMaterial` | Sprites |

## Device Loss Handling

```javascript
// Listen for device loss
renderer.backend.device.lost.then((info) => {
  if (info.reason === 'unknown') {
    // Unexpected loss - recover
    renderer.dispose();
    initWebGPU();  // Reinitialize
  }
});

// Simulate loss for testing
renderer.backend.device.destroy();
```

| Loss Reason | Meaning |
|-------------|---------|
| `'destroyed'` | Intentional via `destroy()` |
| `'unknown'` | Unexpected (driver crash, timeout, etc.) |

**Recovery tips:**
- Always get fresh adapter before new device
- Save/restore application state (not transient data)
- Use Chrome `about:gpucrash` to test real GPU crashes

## Compute Shader Built-ins

| Node | Description |
|------|-------------|
| `instanceIndex` | Current instance/invocation index |
| `vertexIndex` | Current vertex index |
| `drawIndex` | Current draw call index |
| `globalId` | Global invocation position (uvec3) |
| `localId` | Local workgroup position (uvec3) |
| `workgroupId` | Workgroup index (uvec3) |
| `numWorkgroups` | Number of workgroups dispatched (uvec3) |
| `subgroupSize` | Size of the subgroup |

## Version Notes

**r178+:**
- `PI2` is deprecated → use `TWO_PI`
- `transformedNormalView` → use `normalView`
- `transformedNormalWorld` → use `normalWorld`

**r171+:**
- Recommended minimum version for stable TSL
- Requires separate `three/webgpu` import map entry

## Resources

- [TSL Wiki](https://github.com/mrdoob/three.js/wiki/Three.js-Shading-Language)
- [TSL Docs](https://threejs.org/docs/pages/TSL.html)
- [WebGPU Examples](https://github.com/mrdoob/three.js/tree/master/examples)
- [Three.js Docs](https://threejs.org/docs/)
- [WebGPU Best Practices - Device Loss](https://toji.dev/webgpu-best-practices/device-loss)
```

## File: `skills/webgpu-threejs-tsl/SKILL.md`
```markdown
---
name: webgpu-threejs-tsl
description: Comprehensive guide for developing WebGPU-enabled Three.js applications using TSL (Three.js Shading Language). Covers WebGPU renderer setup, TSL syntax and node materials, compute shaders, post-processing effects, and WGSL integration. Use this skill when working with Three.js WebGPU, TSL shaders, node materials, or GPU compute in Three.js.
---

# WebGPU Three.js with TSL

TSL (Three.js Shading Language) is a node-based shader abstraction that lets you write GPU shaders in JavaScript instead of GLSL/WGSL strings.

## Quick Start

```javascript
import * as THREE from 'three/webgpu';
import { color, time, oscSine } from 'three/tsl';

const renderer = new THREE.WebGPURenderer();
await renderer.init();

const material = new THREE.MeshStandardNodeMaterial();
material.colorNode = color(0xff0000).mul(oscSine(time));
```

## Skill Contents

### Documentation
- `docs/core-concepts.md` - Types, operators, uniforms, control flow
- `docs/materials.md` - Node materials and all properties
- `docs/compute-shaders.md` - GPU compute with instanced arrays
- `docs/post-processing.md` - Built-in and custom effects
- `docs/wgsl-integration.md` - Custom WGSL functions
- `docs/device-loss.md` - Handling GPU device loss and recovery

### Examples
- `examples/basic-setup.js` - Minimal WebGPU project
- `examples/custom-material.js` - Custom shader material
- `examples/particle-system.js` - GPU compute particles
- `examples/post-processing.js` - Effect pipeline
- `examples/earth-shader.js` - Complete Earth with atmosphere

### Templates
- `templates/webgpu-project.js` - Starter project template
- `templates/compute-shader.js` - Compute shader template

### Reference
- `REFERENCE.md` - Quick reference cheatsheet

## Key Concepts

### Import Pattern
```javascript
// Always use the WebGPU entry point
import * as THREE from 'three/webgpu';
import { /* TSL functions */ } from 'three/tsl';
```

### Node Materials
Replace standard material properties with TSL nodes:
```javascript
material.colorNode = texture(map);        // instead of material.map
material.roughnessNode = float(0.5);      // instead of material.roughness
material.positionNode = displaced;         // vertex displacement
```

### Method Chaining
TSL uses method chaining for operations:
```javascript
// Instead of: sin(time * 2.0 + offset) * 0.5 + 0.5
time.mul(2.0).add(offset).sin().mul(0.5).add(0.5)
```

### Custom Functions
Use `Fn()` for reusable shader logic:
```javascript
const fresnel = Fn(([power = 2.0]) => {
  const nDotV = normalWorld.dot(viewDir).saturate();
  return float(1.0).sub(nDotV).pow(power);
});
```

## When to Use This Skill

- Setting up Three.js with WebGPU renderer
- Creating custom shader materials with TSL
- Writing GPU compute shaders
- Building post-processing pipelines
- Migrating from GLSL to TSL
- Implementing visual effects (particles, water, terrain, etc.)

## Resources

- [Three.js TSL Wiki](https://github.com/mrdoob/three.js/wiki/Three.js-Shading-Language)
- [WebGPU Examples](https://github.com/mrdoob/three.js/tree/master/examples) (files prefixed with `webgpu_`)
```

## File: `skills/webgpu-threejs-tsl/docs/compute-shaders.md`
```markdown
# TSL Compute Shaders

Compute shaders run on the GPU for parallel processing of data. TSL makes them accessible through JavaScript.

## Basic Setup

```javascript
import * as THREE from 'three/webgpu';
import { Fn, instancedArray, instanceIndex, vec3 } from 'three/tsl';

// Create storage buffer
const count = 100000;
const positions = instancedArray(count, 'vec3');

// Create compute shader
const computeShader = Fn(() => {
  const position = positions.element(instanceIndex);
  position.x.addAssign(0.01);
})().compute(count);

// Execute
renderer.compute(computeShader);
```

## Storage Buffers

### Instanced Arrays

```javascript
import { instancedArray } from 'three/tsl';

// Create typed storage buffers
const positions = instancedArray(count, 'vec3');
const velocities = instancedArray(count, 'vec3');
const colors = instancedArray(count, 'vec4');
const indices = instancedArray(count, 'uint');
const values = instancedArray(count, 'float');
```

### Accessing Elements

```javascript
const computeShader = Fn(() => {
  // Get element at current index
  const position = positions.element(instanceIndex);
  const velocity = velocities.element(instanceIndex);

  // Read values
  const x = position.x;
  const speed = velocity.length();

  // Write values
  position.assign(vec3(0, 0, 0));
  position.x.assign(1.0);
  position.addAssign(velocity);
})().compute(count);
```

### Accessing Other Elements

```javascript
const computeShader = Fn(() => {
  const myIndex = instanceIndex;
  const neighborIndex = myIndex.add(1).mod(count);

  const myPos = positions.element(myIndex);
  const neighborPos = positions.element(neighborIndex);

  // Calculate distance to neighbor
  const dist = myPos.distance(neighborPos);
})().compute(count);
```

## Compute Shader Patterns

### Initialize Particles

```javascript
const computeInit = Fn(() => {
  const position = positions.element(instanceIndex);
  const velocity = velocities.element(instanceIndex);

  // Random positions using hash
  position.x.assign(hash(instanceIndex).mul(10).sub(5));
  position.y.assign(hash(instanceIndex.add(1)).mul(10).sub(5));
  position.z.assign(hash(instanceIndex.add(2)).mul(10).sub(5));

  // Zero velocity
  velocity.assign(vec3(0));
})().compute(count);

// Run once at startup
await renderer.computeAsync(computeInit);
```

### Physics Update

```javascript
const gravity = uniform(-9.8);
const deltaTimeUniform = uniform(0);
const groundY = uniform(0);

const computeUpdate = Fn(() => {
  const position = positions.element(instanceIndex);
  const velocity = velocities.element(instanceIndex);
  const dt = deltaTimeUniform;

  // Apply gravity
  velocity.y.addAssign(gravity.mul(dt));

  // Update position
  position.addAssign(velocity.mul(dt));

  // Ground collision
  If(position.y.lessThan(groundY), () => {
    position.y.assign(groundY);
    velocity.y.assign(velocity.y.negate().mul(0.8)); // Bounce
    velocity.xz.mulAssign(0.95); // Friction
  });
})().compute(count);

// In animation loop
function animate() {
  deltaTimeUniform.value = clock.getDelta();
  renderer.compute(computeUpdate);
  renderer.render(scene, camera);
}
```

### Attraction to Point

```javascript
const attractorPos = uniform(new THREE.Vector3(0, 0, 0));
const attractorStrength = uniform(1.0);

const computeAttract = Fn(() => {
  const position = positions.element(instanceIndex);
  const velocity = velocities.element(instanceIndex);

  // Direction to attractor
  const toAttractor = attractorPos.sub(position);
  const distance = toAttractor.length();
  const direction = toAttractor.normalize();

  // Apply force (inverse square falloff)
  const force = direction.mul(attractorStrength).div(distance.mul(distance).add(0.1));
  velocity.addAssign(force.mul(deltaTimeUniform));
})().compute(count);
```

### Neighbor Interaction (Boids-like)

```javascript
const computeBoids = Fn(() => {
  const myPos = positions.element(instanceIndex);
  const myVel = velocities.element(instanceIndex);

  const separation = vec3(0).toVar();
  const alignment = vec3(0).toVar();
  const cohesion = vec3(0).toVar();
  const neighborCount = int(0).toVar();

  // Check nearby particles
  Loop(count, ({ i }) => {
    If(i.notEqual(instanceIndex), () => {
      const otherPos = positions.element(i);
      const otherVel = velocities.element(i);
      const dist = myPos.distance(otherPos);

      If(dist.lessThan(2.0), () => {
        // Separation
        const diff = myPos.sub(otherPos).normalize().div(dist);
        separation.addAssign(diff);

        // Alignment
        alignment.addAssign(otherVel);

        // Cohesion
        cohesion.addAssign(otherPos);

        neighborCount.addAssign(1);
      });
    });
  });

  If(neighborCount.greaterThan(0), () => {
    const n = neighborCount.toFloat();
    alignment.divAssign(n);
    cohesion.divAssign(n);
    cohesion.assign(cohesion.sub(myPos));

    myVel.addAssign(separation.mul(0.05));
    myVel.addAssign(alignment.sub(myVel).mul(0.05));
    myVel.addAssign(cohesion.mul(0.05));
  });

  // Limit speed
  const speed = myVel.length();
  If(speed.greaterThan(2.0), () => {
    myVel.assign(myVel.normalize().mul(2.0));
  });

  myPos.addAssign(myVel.mul(deltaTimeUniform));
})().compute(count);
```

## Workgroups and Synchronization

### Workgroup Size

```javascript
// Default workgroup size is typically 64 or 256
const computeShader = Fn(() => {
  // shader code
})().compute(count, { workgroupSize: 64 });
```

### Barriers

```javascript
import { workgroupBarrier, storageBarrier, textureBarrier } from 'three/tsl';

const computeShader = Fn(() => {
  // Write data
  sharedData.element(localIndex).assign(value);

  // Ensure all workgroup threads reach this point
  workgroupBarrier();

  // Now safe to read data written by other threads
  const neighborValue = sharedData.element(localIndex.add(1));
})().compute(count);
```

## Atomic Operations

For thread-safe read-modify-write operations:

```javascript
import { atomicAdd, atomicSub, atomicMax, atomicMin, atomicAnd, atomicOr, atomicXor } from 'three/tsl';

const counter = instancedArray(1, 'uint');

const computeShader = Fn(() => {
  // Atomically increment counter
  atomicAdd(counter.element(0), 1);

  // Atomic max
  atomicMax(maxValue.element(0), localValue);
})().compute(count);
```

## Using Compute Results in Materials

### Instanced Mesh with Computed Positions

```javascript
// Create instanced mesh
const geometry = new THREE.SphereGeometry(0.1, 16, 16);
const material = new THREE.MeshStandardNodeMaterial();

// Use computed positions
material.positionNode = positions.element(instanceIndex);

// Optionally use computed colors
material.colorNode = colors.element(instanceIndex);

const mesh = new THREE.InstancedMesh(geometry, material, count);
scene.add(mesh);
```

### Points with Computed Positions

```javascript
const geometry = new THREE.BufferGeometry();
geometry.setAttribute('position', new THREE.Float32BufferAttribute(new Float32Array(count * 3), 3));

const material = new THREE.PointsNodeMaterial();
material.positionNode = positions.element(instanceIndex);
material.colorNode = colors.element(instanceIndex);
material.sizeNode = float(5.0);

const points = new THREE.Points(geometry, material);
scene.add(points);
```

## Execution Methods

```javascript
// Synchronous compute (blocks until complete)
renderer.compute(computeShader);

// Asynchronous compute (returns promise)
await renderer.computeAsync(computeShader);

// Multiple computes
renderer.compute(computeInit);
renderer.compute(computePhysics);
renderer.compute(computeCollisions);
```

## Reading Back Data (GPU to CPU)

```javascript
// Create buffer for readback
const readBuffer = new Float32Array(count * 3);

// Read data back from GPU
await renderer.readRenderTargetPixelsAsync(
  computeTexture,
  0, 0, width, height,
  readBuffer
);
```

## Complete Example: Particle System

```javascript
import * as THREE from 'three/webgpu';
import {
  Fn, If, instancedArray, instanceIndex, uniform,
  vec3, float, hash, time
} from 'three/tsl';

// Setup
const count = 50000;
const positions = instancedArray(count, 'vec3');
const velocities = instancedArray(count, 'vec3');
const lifetimes = instancedArray(count, 'float');

// Uniforms
const emitterPos = uniform(new THREE.Vector3(0, 0, 0));
const gravity = uniform(-2.0);
const dt = uniform(0);

// Initialize
const computeInit = Fn(() => {
  const pos = positions.element(instanceIndex);
  const vel = velocities.element(instanceIndex);
  const life = lifetimes.element(instanceIndex);

  pos.assign(emitterPos);

  // Random velocity in cone
  const angle = hash(instanceIndex).mul(Math.PI * 2);
  const speed = hash(instanceIndex.add(1)).mul(2).add(1);
  vel.x.assign(angle.cos().mul(speed).mul(0.3));
  vel.y.assign(speed);
  vel.z.assign(angle.sin().mul(speed).mul(0.3));

  // Random lifetime
  life.assign(hash(instanceIndex.add(2)).mul(2).add(1));
})().compute(count);

// Update
const computeUpdate = Fn(() => {
  const pos = positions.element(instanceIndex);
  const vel = velocities.element(instanceIndex);
  const life = lifetimes.element(instanceIndex);

  // Apply gravity
  vel.y.addAssign(gravity.mul(dt));

  // Update position
  pos.addAssign(vel.mul(dt));

  // Decrease lifetime
  life.subAssign(dt);

  // Respawn dead particles
  If(life.lessThan(0), () => {
    pos.assign(emitterPos);
    const angle = hash(instanceIndex.add(time.mul(1000))).mul(Math.PI * 2);
    const speed = hash(instanceIndex.add(time.mul(1000)).add(1)).mul(2).add(1);
    vel.x.assign(angle.cos().mul(speed).mul(0.3));
    vel.y.assign(speed);
    vel.z.assign(angle.sin().mul(speed).mul(0.3));
    life.assign(hash(instanceIndex.add(time.mul(1000)).add(2)).mul(2).add(1));
  });
})().compute(count);

// Material
const material = new THREE.PointsNodeMaterial();
material.positionNode = positions.element(instanceIndex);
material.sizeNode = float(3.0);
material.colorNode = vec3(1, 0.5, 0.2);

// Geometry (dummy positions)
const geometry = new THREE.BufferGeometry();
geometry.setAttribute('position', new THREE.Float32BufferAttribute(new Float32Array(count * 3), 3));

const points = new THREE.Points(geometry, material);
scene.add(points);

// Init
await renderer.computeAsync(computeInit);

// Animation loop
function animate() {
  dt.value = Math.min(clock.getDelta(), 0.1);
  renderer.compute(computeUpdate);
  renderer.render(scene, camera);
}
```
```

## File: `skills/webgpu-threejs-tsl/docs/core-concepts.md`
```markdown
# TSL Core Concepts

## Types and Constructors

### Scalar Types
```javascript
import { float, int, uint, bool } from 'three/tsl';

const f = float(1.0);
const i = int(42);
const u = uint(100);
const b = bool(true);
```

### Vector Types
```javascript
import { vec2, vec3, vec4, color } from 'three/tsl';

const v2 = vec2(1.0, 2.0);
const v3 = vec3(1.0, 2.0, 3.0);
const v4 = vec4(1.0, 2.0, 3.0, 1.0);

// Color (RGB, accepts hex or components)
const c = color(0xff0000);     // Red
const c2 = color(1, 0.5, 0);   // Orange
```

### Matrix Types
```javascript
import { mat2, mat3, mat4 } from 'three/tsl';

const m3 = mat3();
const m4 = mat4();
```

### Type Conversion
```javascript
const v = vec3(1, 2, 3);
const v4 = v.toVec4(1.0);      // vec4(1, 2, 3, 1)
const f = int(42).toFloat();   // 42.0
const c = v.toColor();         // Convert to color
```

## Vector Swizzling

Access and reorder vector components using standard notation:

```javascript
const v = vec3(1.0, 2.0, 3.0);

// Single component access
v.x  // 1.0
v.y  // 2.0
v.z  // 3.0

// Multiple components
v.xy   // vec2(1.0, 2.0)
v.xyz  // vec3(1.0, 2.0, 3.0)

// Reorder components
v.zyx  // vec3(3.0, 2.0, 1.0)
v.xxy  // vec3(1.0, 1.0, 2.0)
v.rrr  // vec3(1.0, 1.0, 1.0) - same as xxx

// Alternative accessors (all equivalent)
v.xyz  // position
v.rgb  // color
v.stp  // texture coordinates
```

## Uniforms

Uniforms pass values from JavaScript to shaders:

```javascript
import { uniform } from 'three/tsl';
import * as THREE from 'three/webgpu';

// Create uniforms
const myColor = uniform(new THREE.Color(0x0066ff));
const myFloat = uniform(0.5);
const myVec3 = uniform(new THREE.Vector3(1, 2, 3));

// Update at runtime
myColor.value.set(0xff0000);
myFloat.value = 0.8;
myVec3.value.set(4, 5, 6);

// Use in material
material.colorNode = myColor;
```

### Auto-Updating Uniforms

```javascript
// Update every frame
const animatedValue = uniform(0).onFrameUpdate((frame) => {
  return Math.sin(frame.time);
});

// Update per object render
const perObjectValue = uniform(0).onObjectUpdate((object) => {
  return object.userData.customValue;
});

// Update once per render cycle
const renderValue = uniform(0).onRenderUpdate((state) => {
  return state.delta;
});
```

## Operators

### Arithmetic
```javascript
// Method chaining (preferred)
const result = a.add(b).mul(c).sub(d).div(e);

// Individual operations
a.add(b)   // a + b
a.sub(b)   // a - b
a.mul(b)   // a * b
a.div(b)   // a / b
a.mod(b)   // a % b
a.negate() // -a
```

### Comparison
```javascript
a.equal(b)            // a == b
a.notEqual(b)         // a != b
a.lessThan(b)         // a < b
a.greaterThan(b)      // a > b
a.lessThanEqual(b)    // a <= b
a.greaterThanEqual(b) // a >= b
```

### Logical
```javascript
a.and(b)   // a && b
a.or(b)    // a || b
a.not()    // !a
a.xor(b)   // a ^ b
```

### Bitwise
```javascript
a.bitAnd(b)      // a & b
a.bitOr(b)       // a | b
a.bitXor(b)      // a ^ b
a.bitNot()       // ~a
a.shiftLeft(n)   // a << n
a.shiftRight(n)  // a >> n
```

### Assignment (for variables)
```javascript
const v = vec3(0).toVar();  // Create mutable variable

v.assign(vec3(1, 2, 3));    // v = vec3(1, 2, 3)
v.addAssign(vec3(1));       // v += vec3(1)
v.subAssign(vec3(1));       // v -= vec3(1)
v.mulAssign(2.0);           // v *= 2.0
v.divAssign(2.0);           // v /= 2.0
```

## Variables

### Mutable Variables
```javascript
// Create mutable variable with toVar()
const myVar = vec3(1, 0, 0).toVar();
myVar.assign(vec3(0, 1, 0));
myVar.addAssign(vec3(0, 0, 1));

// Name the variable (useful for debugging)
const named = vec3(0).toVar('myPosition');
```

### Constants
```javascript
// Create compile-time constant
const PI_HALF = float(Math.PI / 2).toConst();
```

### Properties (named values for shader stages)
```javascript
import { property } from 'three/tsl';

// Create named property
const myProp = property('vec3', 'customColor');
myProp.assign(vec3(1, 0, 0));
```

## Control Flow

### Conditionals

```javascript
import { If, select } from 'three/tsl';

// If-ElseIf-Else
const result = vec3(0).toVar();

If(value.greaterThan(0.5), () => {
  result.assign(vec3(1, 0, 0));  // Red
}).ElseIf(value.greaterThan(0.25), () => {
  result.assign(vec3(0, 1, 0));  // Green
}).Else(() => {
  result.assign(vec3(0, 0, 1));  // Blue
});

// Ternary operator (select)
const color = select(
  condition,           // if true
  vec3(1, 0, 0),      // return this
  vec3(0, 0, 1)       // else return this
);
```

### Switch-Case

```javascript
import { Switch } from 'three/tsl';

const col = vec3(0).toVar();

Switch(intValue)
  .Case(0, () => { col.assign(color(1, 0, 0)); })
  .Case(1, () => { col.assign(color(0, 1, 0)); })
  .Case(2, () => { col.assign(color(0, 0, 1)); })
  .Default(() => { col.assign(color(1, 1, 1)); });
```

### Loops

```javascript
import { Loop, Break, Continue } from 'three/tsl';

// Simple loop (0 to 9)
const sum = float(0).toVar();
Loop(10, ({ i }) => {
  sum.addAssign(float(i));
});

// Ranged loop with options
Loop({ start: int(0), end: int(count), type: 'int' }, ({ i }) => {
  // Loop body
});

// Nested loops
Loop(width, height, ({ i, j }) => {
  // i = outer loop index
  // j = inner loop index
});

// Loop control
Loop(100, ({ i }) => {
  If(shouldStop, () => {
    Break();  // Exit loop
  });
  If(shouldSkip, () => {
    Continue();  // Skip to next iteration
  });
});
```

### Flow Control

```javascript
import { Discard, Return } from 'three/tsl';

// Discard fragment (make transparent)
If(alpha.lessThan(0.5), () => {
  Discard();
});

// Return from function
const myFn = Fn(() => {
  If(condition, () => {
    Return(vec3(1, 0, 0));
  });
  return vec3(0, 0, 1);
});
```

## Custom Functions with Fn()

### Basic Function
```javascript
import { Fn } from 'three/tsl';

const addVectors = Fn(([a, b]) => {
  return a.add(b);
});

// Usage
const result = addVectors(vec3(1, 0, 0), vec3(0, 1, 0));
```

### Default Parameters
```javascript
const oscillate = Fn(([frequency = 1.0, amplitude = 1.0]) => {
  return time.mul(frequency).sin().mul(amplitude);
});

// Call variations
oscillate();           // Uses defaults
oscillate(2.0);        // frequency = 2.0
oscillate(2.0, 0.5);   // frequency = 2.0, amplitude = 0.5
```

### Named Parameters (Object Style)
```javascript
const createGradient = Fn(({ colorA = vec3(0), colorB = vec3(1), t = 0.5 }) => {
  return mix(colorA, colorB, t);
});

// Call with named parameters
createGradient({ colorA: vec3(1, 0, 0), t: uv().x });
```

### Function with Context
```javascript
// Access shader context
const customShader = Fn(({ material, geometry, object }) => {
  if (material.userData.customColor) {
    return uniform(material.userData.customColor);
  }
  return vec3(1);
});
```

## Time and Animation

```javascript
import { time, deltaTime } from 'three/tsl';

// time - seconds since start
const rotation = time.mul(0.5);  // Half rotation per second

// deltaTime - time since last frame
const velocity = speed.mul(deltaTime);
```

### Oscillators

```javascript
import { oscSine, oscSquare, oscTriangle, oscSawtooth } from 'three/tsl';

// All oscillators return 0-1 range
oscSine(time)      // Smooth sine wave
oscSquare(time)    // Square wave (0 or 1)
oscTriangle(time)  // Triangle wave
oscSawtooth(time)  // Sawtooth wave

// Custom frequency
oscSine(time.mul(2.0))  // 2Hz oscillation
```

## Math Functions

### Basic Math
```javascript
import { abs, sign, floor, ceil, fract, mod, min, max, clamp } from 'three/tsl';

abs(x)           // Absolute value
sign(x)          // -1, 0, or 1
floor(x)         // Round down
ceil(x)          // Round up
fract(x)         // Fractional part (x - floor(x))
mod(x, y)        // Modulo
min(x, y)        // Minimum
max(x, y)        // Maximum
clamp(x, 0, 1)   // Clamp to range
```

### Trigonometry
```javascript
import { sin, cos, tan, asin, acos, atan, atan2 } from 'three/tsl';

sin(x)
cos(x)
tan(x)
asin(x)
acos(x)
atan(x)
atan2(y, x)
```

### Exponential
```javascript
import { pow, exp, log, sqrt, inverseSqrt } from 'three/tsl';

pow(x, 2.0)      // x^2
exp(x)           // e^x
log(x)           // Natural log
sqrt(x)          // Square root
inverseSqrt(x)   // 1 / sqrt(x)
```

### Interpolation
```javascript
import { mix, step, smoothstep } from 'three/tsl';

mix(a, b, 0.5)              // Linear interpolation
step(0.5, x)                // 0 if x < 0.5, else 1
smoothstep(0.0, 1.0, x)     // Smooth 0-1 transition
```

### Vector Math
```javascript
import { length, distance, dot, cross, normalize, reflect, refract } from 'three/tsl';

length(v)              // Vector length
distance(a, b)         // Distance between points
dot(a, b)              // Dot product
cross(a, b)            // Cross product (vec3 only)
normalize(v)           // Unit vector
reflect(incident, normal)
refract(incident, normal, eta)
```

### Constants
```javascript
import { PI, TWO_PI, HALF_PI, EPSILON } from 'three/tsl';

PI        // 3.14159...
TWO_PI    // 6.28318...
HALF_PI   // 1.57079...
EPSILON   // Very small number
```

## Utility Functions

```javascript
import { hash, checker, remap, range, rotate } from 'three/tsl';

// Pseudo-random hash
hash(seed)                    // Returns 0-1

// Checkerboard pattern
checker(uv())                 // Returns 0 or 1

// Remap value from one range to another
remap(x, 0, 1, -1, 1)        // Map 0-1 to -1 to 1

// Generate value in range
range(min, max)               // Random in range (per instance)

// Rotate 2D vector
rotate(vec2(1, 0), angle)
```
```

## File: `skills/webgpu-threejs-tsl/docs/device-loss.md`
```markdown
# WebGPU Device Loss Handling

## What Is Device Loss?

Device loss occurs when the GPU driver cannot continue processing commands. Causes include:

- Driver crashes
- Extreme resource pressure
- Long-running shaders (GPU watchdog triggers after ~10 seconds)
- Driver updates
- Significant device configuration changes

When a device is lost, the `GPUDevice` object and **all objects created with it become unusable**. All buffers, textures, pipelines, and GPU memory are discarded.

## Listening for Device Loss

Detect loss by attaching a callback to the device's `lost` promise:

```javascript
const adapter = await navigator.gpu.requestAdapter();
if (!adapter) { return; }
const device = await adapter.requestDevice();

device.lost.then((info) => {
  console.error('WebGPU device lost:', info.message);
  // Handle recovery
});
```

**Important:** Don't `await` this promise directly - it will block indefinitely if loss never occurs.

### Device Loss Information

The `GPUDeviceLostInfo` object provides:

| Property | Description |
|----------|-------------|
| `reason` | `'destroyed'` (intentional via `destroy()`) or `'unknown'` (unexpected) |
| `message` | Human-readable debugging info (don't parse programmatically) |

```javascript
device.lost.then((info) => {
  if (info.reason === 'unknown') {
    // Unexpected loss - attempt recovery
    handleUnexpectedDeviceLoss();
  } else {
    // Intentional destruction - expected behavior
  }
});
```

### Devices Starting Lost

`adapter.requestDevice()` always returns a `GPUDevice`, but it may already be lost if creation failed. This occurs when the adapter was "consumed" (used previously) or "expired."

**Best practice:** Always get a new adapter right before requesting a device.

## Recovery Strategies

### Minimal Recovery (Page Reload)

For simple applications:

```javascript
device.lost.then((info) => {
  if (info.reason === 'unknown') {
    // Warn user before reload
    alert('Graphics error occurred. The page will reload.');
    location.reload();
  }
});
```

### Restart GPU Content Only (Recommended for Three.js)

Recreate the device and reconfigure the canvas without full page reload:

```javascript
import * as THREE from 'three/webgpu';

let renderer;
let scene, camera;

async function initWebGPU() {
  renderer = new THREE.WebGPURenderer();
  await renderer.init();

  // Access the underlying WebGPU device
  const device = renderer.backend.device;

  device.lost.then((info) => {
    console.error('Device lost:', info.message);
    if (info.reason === 'unknown') {
      // Dispose current renderer
      renderer.dispose();
      // Reinitialize
      initWebGPU();
    }
  });

  // Configure canvas
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  // Recreate scene content
  setupScene();
}

function setupScene() {
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  // ... add meshes, lights, etc.
}

initWebGPU();
```

### Restore with Application State

For applications with user progress or configuration:

```javascript
let appState = {
  cameraPosition: { x: 0, y: 5, z: 10 },
  settings: {},
  // Don't save transient data like particle positions
};

// Save state periodically
function saveState() {
  appState.cameraPosition = {
    x: camera.position.x,
    y: camera.position.y,
    z: camera.position.z
  };
  localStorage.setItem('appState', JSON.stringify(appState));
}

// Restore on recovery
async function initWebGPU() {
  renderer = new THREE.WebGPURenderer();
  await renderer.init();

  const savedState = localStorage.getItem('appState');
  if (savedState) {
    appState = JSON.parse(savedState);
  }

  setupScene();

  // Restore camera position
  camera.position.set(
    appState.cameraPosition.x,
    appState.cameraPosition.y,
    appState.cameraPosition.z
  );

  renderer.backend.device.lost.then((info) => {
    if (info.reason === 'unknown') {
      saveState();
      renderer.dispose();
      initWebGPU();
    }
  });
}
```

## When Recovery Fails

If `requestAdapter()` returns `null` after device loss, the OS or browser has blocked GPU access:

```javascript
async function initWebGPU() {
  const adapter = await navigator.gpu.requestAdapter();

  if (!adapter) {
    // Check if this is initial failure or post-loss failure
    if (hadPreviousDevice) {
      showMessage('GPU access lost. Please restart your browser.');
    } else {
      showMessage('WebGPU is not supported on this device.');
    }
    return;
  }

  // Continue with device creation...
}
```

## Testing Device Loss

### Using destroy()

Call `device.destroy()` to simulate loss:

```javascript
let simulatedLoss = false;

function simulateDeviceLoss() {
  simulatedLoss = true;
  renderer.backend.device.destroy();
}

// In your device.lost handler:
device.lost.then((info) => {
  if (info.reason === 'unknown' || simulatedLoss) {
    simulatedLoss = false;
    // Treat as unexpected loss for testing
    handleDeviceLoss();
  }
});

// Add debug keybinding
window.addEventListener('keydown', (e) => {
  if (e.key === 'L' && e.ctrlKey && e.shiftKey) {
    simulateDeviceLoss();
  }
});
```

**Limitations of destroy():**
- Unmaps buffers immediately (real loss doesn't)
- Always allows device recovery (real loss may not)

### Chrome GPU Process Crash Testing

Navigate to `about:gpucrash` in a **separate tab** to crash the GPU process.

Chrome enforces escalating restrictions:

| Crash | Effect |
|-------|--------|
| 1st | New adapters allowed |
| 2nd within 2 min | Adapter requests fail (resets on page refresh) |
| 3rd within 2 min | All pages blocked (reset after 2 min or browser restart) |
| 3-6 within 5 min | GPU process stops restarting; browser restart required |

### Chrome Testing Flags

Bypass crash limits for development:

```bash
# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --disable-domain-blocking-for-3d-apis \
  --disable-gpu-process-crash-limit

# Windows
chrome.exe --disable-domain-blocking-for-3d-apis --disable-gpu-process-crash-limit

# Linux
google-chrome --disable-domain-blocking-for-3d-apis --disable-gpu-process-crash-limit
```

## Complete Example

```javascript
import * as THREE from 'three/webgpu';
import { color, time, oscSine } from 'three/tsl';

let renderer, scene, camera, mesh;
let hadPreviousDevice = false;

async function init() {
  // Check WebGPU support
  if (!navigator.gpu) {
    showError('WebGPU not supported');
    return;
  }

  // Create renderer
  renderer = new THREE.WebGPURenderer({ antialias: true });

  try {
    await renderer.init();
  } catch (e) {
    if (hadPreviousDevice) {
      showError('GPU recovery failed. Please restart browser.');
    } else {
      showError('Failed to initialize WebGPU.');
    }
    return;
  }

  hadPreviousDevice = true;

  // Setup device loss handler
  const device = renderer.backend.device;
  device.lost.then(handleDeviceLoss);

  // Setup scene
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 5;

  const geometry = new THREE.BoxGeometry();
  const material = new THREE.MeshStandardNodeMaterial();
  material.colorNode = color(0x00ff00).mul(oscSine(time));

  mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  const light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.set(5, 5, 5);
  scene.add(light);
  scene.add(new THREE.AmbientLight(0x404040));

  animate();
}

function handleDeviceLoss(info) {
  console.error('Device lost:', info.reason, info.message);

  if (info.reason === 'unknown') {
    // Cleanup
    if (renderer) {
      renderer.domElement.remove();
      renderer.dispose();
    }

    // Attempt recovery after short delay
    setTimeout(() => {
      init();
    }, 100);
  }
}

function animate() {
  if (!renderer) return;

  requestAnimationFrame(animate);
  mesh.rotation.x += 0.01;
  mesh.rotation.y += 0.01;
  renderer.render(scene, camera);
}

function showError(message) {
  const div = document.createElement('div');
  div.textContent = message;
  div.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);padding:20px;background:#f44;color:#fff;border-radius:8px;';
  document.body.appendChild(div);
}

init();
```

## Best Practices

1. **Always listen for device loss** - Even if you just show an error message
2. **Get a fresh adapter before each device request** - The GPU hardware may have changed
3. **Don't parse the message field** - It's implementation-specific and changes between browsers
4. **Save critical application state** - Restore user progress after recovery
5. **Don't save transient state** - Particle positions, physics state can be reset
6. **Test your recovery path** - Use `destroy()` and Chrome's `about:gpucrash`
7. **Handle adapter failure gracefully** - Distinguish between initial failure and post-loss failure
8. **Add a short delay before recovery** - Give the system time to stabilize
```

## File: `skills/webgpu-threejs-tsl/docs/materials.md`
```markdown
# TSL Node Materials

## Available Material Types

| Material | Description |
|----------|-------------|
| `MeshBasicNodeMaterial` | Unlit, no lighting calculations |
| `MeshStandardNodeMaterial` | PBR material with metalness/roughness |
| `MeshPhysicalNodeMaterial` | Advanced PBR with clearcoat, transmission, etc. |
| `MeshPhongNodeMaterial` | Classic Phong shading |
| `MeshToonNodeMaterial` | Cel/toon shading |
| `MeshLambertNodeMaterial` | Diffuse-only lighting |
| `MeshNormalNodeMaterial` | Visualize normals |
| `MeshMatcapNodeMaterial` | Matcap texture shading |
| `PointsNodeMaterial` | For point clouds |
| `LineBasicNodeMaterial` | For lines |
| `LineDashedNodeMaterial` | For dashed lines |
| `SpriteNodeMaterial` | For sprites/billboards |

## Creating Node Materials

```javascript
import * as THREE from 'three/webgpu';

// Standard PBR material
const material = new THREE.MeshStandardNodeMaterial();

// Physical material with advanced features
const physicalMat = new THREE.MeshPhysicalNodeMaterial();

// Unlit material
const basicMat = new THREE.MeshBasicNodeMaterial();
```

## Material Properties

### Color and Opacity

```javascript
import { texture, color, float } from 'three/tsl';

// Color from texture
material.colorNode = texture(diffuseMap);

// Solid color
material.colorNode = color(0xff0000);

// Computed color
material.colorNode = positionLocal.normalize();

// Opacity (requires material.transparent = true)
material.opacityNode = float(0.8);
material.transparent = true;

// Alpha test threshold
material.alphaTestNode = float(0.5);
```

### PBR Properties (MeshStandardNodeMaterial)

```javascript
import { texture, float, color } from 'three/tsl';

// Metalness (0 = dielectric, 1 = metal)
material.metalnessNode = texture(metalMap).r;
material.metalnessNode = float(0.0);

// Roughness (0 = smooth/mirror, 1 = rough)
material.roughnessNode = texture(roughnessMap).r;
material.roughnessNode = float(0.5);

// Emissive (self-illumination)
material.emissiveNode = color(0xff0000).mul(2.0);
material.emissiveNode = texture(emissiveMap);
```

### Normal Mapping

```javascript
import { texture, normalMap, bumpMap } from 'three/tsl';

// Normal map
material.normalNode = normalMap(texture(normalMapTexture));

// Normal map with strength
material.normalNode = normalMap(texture(normalMapTexture), float(0.5));

// Bump map (height to normal)
material.normalNode = bumpMap(texture(heightMap), 0.05);
```

### Physical Properties (MeshPhysicalNodeMaterial)

```javascript
const material = new THREE.MeshPhysicalNodeMaterial();

// Clearcoat (car paint effect)
material.clearcoatNode = float(1.0);
material.clearcoatRoughnessNode = float(0.1);
material.clearcoatNormalNode = normalMap(texture(clearcoatNormalMap));

// Transmission (glass/translucency)
material.transmissionNode = float(0.9);
material.thicknessNode = float(0.5);
material.attenuationDistanceNode = float(1.0);
material.attenuationColorNode = color(0xffffff);

// Iridescence (soap bubble effect)
material.iridescenceNode = float(1.0);
material.iridescenceIORNode = float(1.3);
material.iridescenceThicknessNode = float(400);

// Sheen (fabric effect)
material.sheenNode = float(1.0);
material.sheenRoughnessNode = float(0.5);
material.sheenColorNode = color(0xffffff);

// Anisotropy (brushed metal)
material.anisotropyNode = float(1.0);
material.anisotropyRotationNode = float(0);

// Specular
material.specularIntensityNode = float(1.0);
material.specularColorNode = color(0xffffff);

// Index of Refraction
material.iorNode = float(1.5);

// Dispersion (rainbow effect in glass)
material.dispersionNode = float(0.0);
```

### Environment and Lighting

```javascript
import { cubeTexture, envMap } from 'three/tsl';

// Environment map reflection
material.envMapNode = cubeTexture(envCubeMap);

// Custom lights
material.lightsNode = lights();
```

## Vertex Manipulation

### Position Displacement

```javascript
import { positionLocal, normalLocal, texture } from 'three/tsl';

// Displace vertices along normals
const displacement = texture(heightMap).r.mul(0.1);
material.positionNode = positionLocal.add(normalLocal.mul(displacement));

// Wave displacement
const wave = positionLocal.x.add(time).sin().mul(0.1);
material.positionNode = positionLocal.add(vec3(0, wave, 0));
```

### Custom Vertex Shader

```javascript
// Complete vertex position override
material.vertexNode = customVertexPosition;
```

## Fragment Override

```javascript
// Complete fragment output override
material.fragmentNode = vec4(finalColor, 1.0);

// Output node (respects lighting)
material.outputNode = outputStruct;
```

## Geometry Attributes

### Position Nodes

```javascript
import {
  positionGeometry,  // Original mesh position
  positionLocal,     // Position in model space
  positionWorld,     // Position in world space
  positionView       // Position in camera space
} from 'three/tsl';
```

### Normal Nodes

```javascript
import {
  normalGeometry,    // Original mesh normal
  normalLocal,       // Normal in model space
  normalWorld,       // Normal in world space (use for lighting)
  normalView         // Normal in camera space
} from 'three/tsl';
```

### Tangent/Bitangent

```javascript
import {
  tangentLocal, tangentWorld, tangentView,
  bitangentLocal, bitangentWorld, bitangentView
} from 'three/tsl';
```

### UV Coordinates

```javascript
import { uv } from 'three/tsl';

uv()    // Primary UV set (UV0)
uv(1)   // Secondary UV set (UV1)
uv(2)   // Tertiary UV set (UV2)
```

### Other Attributes

```javascript
import { vertexColor, instanceIndex, vertexIndex } from 'three/tsl';

vertexColor()    // Vertex colors (if present)
instanceIndex    // Index for instanced meshes
vertexIndex      // Current vertex index
```

## Camera Nodes

```javascript
import {
  cameraPosition,         // Camera world position
  cameraNear,             // Near plane distance
  cameraFar,              // Far plane distance
  cameraViewMatrix,       // View matrix
  cameraProjectionMatrix, // Projection matrix
  cameraWorldMatrix       // Camera world matrix
} from 'three/tsl';
```

## Screen Space Nodes

```javascript
import {
  screenUV,         // Screen UV (0-1)
  screenCoordinate, // Pixel coordinates
  screenSize,       // Screen dimensions
  viewportUV,       // Viewport UV
  viewport,         // Viewport dimensions
  depth             // Fragment depth
} from 'three/tsl';
```

## Examples

### Animated Color Material

```javascript
import * as THREE from 'three/webgpu';
import { color, time, oscSine, mix } from 'three/tsl';

const material = new THREE.MeshStandardNodeMaterial();

const colorA = color(0xff0000);
const colorB = color(0x0000ff);
const t = oscSine(time.mul(0.5));

material.colorNode = mix(colorA, colorB, t);
material.roughnessNode = float(0.5);
material.metalnessNode = float(0.0);
```

### Triplanar Mapping Material

```javascript
import * as THREE from 'three/webgpu';
import { texture, triplanarTexture, float } from 'three/tsl';

const material = new THREE.MeshStandardNodeMaterial();

// Apply texture from all three axes
material.colorNode = triplanarTexture(
  texture(diffuseMap),
  null,           // Y-axis texture (optional)
  null,           // Z-axis texture (optional)
  float(0.1)      // Blend sharpness
);
```

### Glass Material

```javascript
import * as THREE from 'three/webgpu';
import { float, color } from 'three/tsl';

const material = new THREE.MeshPhysicalNodeMaterial();

material.colorNode = color(0xffffff);
material.transmissionNode = float(0.95);
material.roughnessNode = float(0.0);
material.metalnessNode = float(0.0);
material.iorNode = float(1.5);
material.thicknessNode = float(0.5);
```

### Fresnel Rim Material

```javascript
import * as THREE from 'three/webgpu';
import {
  color, float, normalWorld, positionWorld,
  cameraPosition, Fn
} from 'three/tsl';

const fresnel = Fn(() => {
  const viewDir = cameraPosition.sub(positionWorld).normalize();
  const nDotV = normalWorld.dot(viewDir).saturate();
  return float(1.0).sub(nDotV).pow(3.0);
});

const material = new THREE.MeshStandardNodeMaterial();
material.colorNode = color(0x222222);
material.emissiveNode = color(0x00ffff).mul(fresnel());
```

### Dissolve Effect Material

```javascript
import * as THREE from 'three/webgpu';
import {
  color, float, hash, positionLocal, uniform,
  If, Discard, smoothstep
} from 'three/tsl';

const threshold = uniform(0.5);

const material = new THREE.MeshStandardNodeMaterial();

const noise = hash(positionLocal.mul(50));

// Discard fragments below threshold
If(noise.lessThan(threshold), () => {
  Discard();
});

// Edge glow
const edge = smoothstep(threshold, threshold.add(0.1), noise);
material.colorNode = color(0x333333);
material.emissiveNode = color(0xff5500).mul(float(1.0).sub(edge));
```
```

## File: `skills/webgpu-threejs-tsl/docs/post-processing.md`
```markdown
# TSL Post-Processing

Post-processing applies effects to the rendered image. TSL provides both built-in effects and the ability to create custom effects.

## Basic Setup

```javascript
import * as THREE from 'three/webgpu';
import { pass } from 'three/tsl';

// Create renderer
const renderer = new THREE.WebGPURenderer();
await renderer.init();

// Create post-processing
const postProcessing = new THREE.PostProcessing(renderer);

// Create scene pass
const scenePass = pass(scene, camera);
const scenePassColor = scenePass.getTextureNode('output');

// Output (passthrough)
postProcessing.outputNode = scenePassColor;

// Render with post-processing
function animate() {
  postProcessing.render();  // Not renderer.render()
}
```

## Built-in Effects

### Bloom

```javascript
import { bloom } from 'three/addons/tsl/display/BloomNode.js';

const scenePass = pass(scene, camera);
const scenePassColor = scenePass.getTextureNode('output');

// Add bloom
const bloomPass = bloom(scenePassColor);

// Configure
bloomPass.threshold.value = 0.5;   // Brightness threshold
bloomPass.strength.value = 1.0;    // Bloom intensity
bloomPass.radius.value = 0.5;      // Blur radius

// Combine original + bloom
postProcessing.outputNode = scenePassColor.add(bloomPass);
```

### Gaussian Blur

```javascript
import { gaussianBlur } from 'three/addons/tsl/display/GaussianBlurNode.js';

const blurred = gaussianBlur(scenePassColor, vec2(2.0)); // Blur strength
postProcessing.outputNode = blurred;
```

### FXAA (Anti-aliasing)

```javascript
import { fxaa } from 'three/addons/tsl/display/FXAANode.js';

postProcessing.outputNode = fxaa(scenePassColor);
```

### SMAA (Anti-aliasing)

```javascript
import { smaa } from 'three/addons/tsl/display/SMAANode.js';

postProcessing.outputNode = smaa(scenePassColor);
```

### Depth of Field

```javascript
import { dof } from 'three/addons/tsl/display/DepthOfFieldNode.js';

const scenePass = pass(scene, camera);
const colorNode = scenePass.getTextureNode('output');
const depthNode = scenePass.getTextureNode('depth');

const dofPass = dof(colorNode, depthNode, {
  focus: 5.0,      // Focus distance
  aperture: 0.025, // Aperture size
  maxblur: 0.01    // Maximum blur
});

postProcessing.outputNode = dofPass;
```

### Motion Blur

```javascript
import { motionBlur } from 'three/addons/tsl/display/MotionBlurNode.js';

const scenePass = pass(scene, camera);
const velocityPass = scenePass.getTextureNode('velocity');

const motionBlurPass = motionBlur(scenePassColor, velocityPass);
postProcessing.outputNode = motionBlurPass;
```

### Screen Space Reflections (SSR)

```javascript
import { ssr } from 'three/addons/tsl/display/SSRNode.js';

const scenePass = pass(scene, camera);
const colorNode = scenePass.getTextureNode('output');
const depthNode = scenePass.getTextureNode('depth');
const normalNode = scenePass.getTextureNode('normal');

const ssrPass = ssr(colorNode, depthNode, normalNode, camera);
postProcessing.outputNode = ssrPass;
```

### Ambient Occlusion (SSAO)

```javascript
import { ao } from 'three/addons/tsl/display/AmbientOcclusionNode.js';

const scenePass = pass(scene, camera);
const depthNode = scenePass.getTextureNode('depth');
const normalNode = scenePass.getTextureNode('normal');

const aoPass = ao(depthNode, normalNode, camera);
postProcessing.outputNode = scenePassColor.mul(aoPass);
```

### Film Grain

```javascript
import { film } from 'three/addons/tsl/display/FilmNode.js';

const filmPass = film(scenePassColor, {
  intensity: 0.5,
  grayscale: false
});
postProcessing.outputNode = filmPass;
```

### Outline

```javascript
import { outline } from 'three/addons/tsl/display/OutlineNode.js';

const outlinePass = outline(scene, camera, selectedObjects, {
  edgeStrength: 3.0,
  edgeGlow: 0.0,
  edgeThickness: 1.0,
  visibleEdgeColor: new THREE.Color(0xffffff),
  hiddenEdgeColor: new THREE.Color(0x190a05)
});

postProcessing.outputNode = scenePassColor.add(outlinePass);
```

### Chromatic Aberration

```javascript
import { chromaticAberration } from 'three/addons/tsl/display/ChromaticAberrationNode.js';

const caPass = chromaticAberration(scenePassColor, {
  offset: vec2(0.002, 0.002)
});
postProcessing.outputNode = caPass;
```

## Color Adjustments

### Grayscale

```javascript
import { grayscale } from 'three/tsl';

postProcessing.outputNode = grayscale(scenePassColor);
```

### Saturation

```javascript
import { saturation } from 'three/tsl';

// 0 = grayscale, 1 = normal, 2 = oversaturated
postProcessing.outputNode = saturation(scenePassColor, 1.5);
```

### Hue Shift

```javascript
import { hue } from 'three/tsl';

// Shift hue by radians
postProcessing.outputNode = hue(scenePassColor, time.mul(0.5));
```

### Vibrance

```javascript
import { vibrance } from 'three/tsl';

postProcessing.outputNode = vibrance(scenePassColor, 0.5);
```

### Posterize

```javascript
import { posterize } from 'three/tsl';

// Reduce color levels
postProcessing.outputNode = posterize(scenePassColor, 8);
```

### Sepia

```javascript
import { sepia } from 'three/addons/tsl/display/SepiaNode.js';

postProcessing.outputNode = sepia(scenePassColor);
```

### 3D LUT

```javascript
import { lut3D } from 'three/addons/tsl/display/Lut3DNode.js';

const lutTexture = new THREE.Data3DTexture(lutData, size, size, size);
postProcessing.outputNode = lut3D(scenePassColor, lutTexture, size);
```

## Custom Post-Processing

### Basic Custom Effect

```javascript
import { Fn, screenUV, float, vec4 } from 'three/tsl';

const customEffect = Fn(() => {
  const color = scenePassColor.toVar();

  // Invert colors
  color.rgb.assign(float(1.0).sub(color.rgb));

  return color;
});

postProcessing.outputNode = customEffect();
```

### Vignette Effect

```javascript
const vignette = Fn(() => {
  const color = scenePassColor.toVar();

  // Distance from center
  const uv = screenUV;
  const dist = uv.sub(0.5).length();

  // Vignette falloff
  const vignette = float(1.0).sub(dist.mul(1.5)).clamp(0, 1);

  color.rgb.mulAssign(vignette);
  return color;
});

postProcessing.outputNode = vignette();
```

### CRT/Scanline Effect

```javascript
import { viewportSharedTexture } from 'three/tsl';

const crtEffect = Fn(() => {
  const uv = screenUV;

  // Sample scene at offset UVs for RGB separation (chromatic aberration)
  const uvR = uv.add(vec2(0.002, 0));
  const uvG = uv;
  const uvB = uv.sub(vec2(0.002, 0));

  // Use viewportSharedTexture to sample at different UV coordinates
  const r = viewportSharedTexture(uvR).r;
  const g = viewportSharedTexture(uvG).g;
  const b = viewportSharedTexture(uvB).b;

  const color = vec4(r, g, b, 1.0).toVar();

  // Scanlines
  const scanline = uv.y.mul(screenSize.y).mul(0.5).sin().mul(0.1).add(0.9);
  color.rgb.mulAssign(scanline);

  // Vignette
  const dist = uv.sub(0.5).length();
  color.rgb.mulAssign(float(1.0).sub(dist.mul(0.5)));

  return color;
});

// Note: For this effect, apply after scene rendering
postProcessing.outputNode = crtEffect();
```

### Pixelate Effect

```javascript
const pixelSize = uniform(8.0);

const pixelate = Fn(() => {
  const uv = screenUV;
  const pixelUV = uv.mul(screenSize).div(pixelSize).floor().mul(pixelSize).div(screenSize);
  return texture(scenePassColor, pixelUV);
});

postProcessing.outputNode = pixelate();
```

### Edge Detection (Sobel)

```javascript
const sobelEdge = Fn(() => {
  const uv = screenUV;
  const texelSize = vec2(1.0).div(screenSize);

  // Sample 3x3 kernel
  const tl = luminance(texture(scenePassColor, uv.add(texelSize.mul(vec2(-1, -1)))));
  const tc = luminance(texture(scenePassColor, uv.add(texelSize.mul(vec2(0, -1)))));
  const tr = luminance(texture(scenePassColor, uv.add(texelSize.mul(vec2(1, -1)))));
  const ml = luminance(texture(scenePassColor, uv.add(texelSize.mul(vec2(-1, 0)))));
  const mr = luminance(texture(scenePassColor, uv.add(texelSize.mul(vec2(1, 0)))));
  const bl = luminance(texture(scenePassColor, uv.add(texelSize.mul(vec2(-1, 1)))));
  const bc = luminance(texture(scenePassColor, uv.add(texelSize.mul(vec2(0, 1)))));
  const br = luminance(texture(scenePassColor, uv.add(texelSize.mul(vec2(1, 1)))));

  // Sobel operators
  const gx = tl.add(ml.mul(2)).add(bl).sub(tr).sub(mr.mul(2)).sub(br);
  const gy = tl.add(tc.mul(2)).add(tr).sub(bl).sub(bc.mul(2)).sub(br);

  const edge = sqrt(gx.mul(gx).add(gy.mul(gy)));

  return vec4(vec3(edge), 1.0);
});

postProcessing.outputNode = sobelEdge();
```

## Multiple Render Targets (MRT)

Access multiple buffers from the scene pass:

```javascript
import { mrt, output } from 'three/tsl';

const scenePass = pass(scene, camera);

// Set up MRT
scenePass.setMRT(mrt({
  output: output,           // Color output
  normal: normalView,       // View-space normals
  depth: depth              // Depth buffer
}));

// Access individual targets
const colorTexture = scenePass.getTextureNode('output');
const normalTexture = scenePass.getTextureNode('normal');
const depthTexture = scenePass.getTextureNode('depth');
```

### Selective Bloom with MRT

Bloom only emissive objects by rendering emissive to a separate target:

```javascript
import { pass, mrt, output, emissive } from 'three/tsl';
import { bloom } from 'three/addons/tsl/display/BloomNode.js';

const postProcessing = new THREE.PostProcessing(renderer);
const scenePass = pass(scene, camera);

// Render both color and emissive to separate targets
scenePass.setMRT(mrt({
  output: output,
  emissive: emissive
}));

// Get the texture nodes
const colorTexture = scenePass.getTextureNode('output');
const emissiveTexture = scenePass.getTextureNode('emissive');

// Apply bloom only to emissive
const bloomPass = bloom(emissiveTexture);
bloomPass.threshold.value = 0.0;  // Bloom all emissive
bloomPass.strength.value = 1.5;
bloomPass.radius.value = 0.5;

// Combine: original color + bloomed emissive
postProcessing.outputNode = colorTexture.add(bloomPass);
```

This approach prevents non-emissive bright areas (like white surfaces) from blooming.

## Chaining Effects

```javascript
const scenePass = pass(scene, camera);
const color = scenePass.getTextureNode('output');

// Chain multiple effects
let output = color;

// 1. Apply bloom
const bloomPass = bloom(output);
output = output.add(bloomPass.mul(0.5));

// 2. Apply color grading
output = saturation(output, 1.2);

// 3. Apply vignette
const dist = screenUV.sub(0.5).length();
const vignette = float(1.0).sub(dist.mul(0.5));
output = output.mul(vignette);

// 4. Apply FXAA
output = fxaa(output);

postProcessing.outputNode = output;
```

## Conditional Effects

```javascript
const effectEnabled = uniform(true);

const conditionalEffect = Fn(() => {
  const color = scenePassColor;
  return select(effectEnabled, grayscale(color), color);
});

postProcessing.outputNode = conditionalEffect();

// Toggle at runtime
effectEnabled.value = false;
```

## Transitions

```javascript
import { transition } from 'three/addons/tsl/display/TransitionNode.js';

const scenePassA = pass(sceneA, camera);
const scenePassB = pass(sceneB, camera);

const transitionProgress = uniform(0);

const transitionPass = transition(
  scenePassA.getTextureNode('output'),
  scenePassB.getTextureNode('output'),
  transitionProgress,
  texture(transitionTexture)  // Optional transition texture
);

postProcessing.outputNode = transitionPass;

// Animate transition
function animate() {
  transitionProgress.value = Math.sin(time) * 0.5 + 0.5;
  postProcessing.render();
}
```
```

## File: `skills/webgpu-threejs-tsl/docs/wgsl-integration.md`
```markdown
# WGSL Integration

TSL allows embedding raw WGSL (WebGPU Shading Language) code when you need direct GPU control.

## wgslFn - Custom WGSL Functions

### Basic Usage

```javascript
import { wgslFn, float, vec3 } from 'three/tsl';

// Define WGSL function
const gammaCorrect = wgslFn(`
  fn gammaCorrect(color: vec3<f32>, gamma: f32) -> vec3<f32> {
    return pow(color, vec3<f32>(1.0 / gamma));
  }
`);

// Use in TSL
material.colorNode = gammaCorrect(inputColor, float(2.2));
```

### Function with Multiple Parameters

```javascript
const blendColors = wgslFn(`
  fn blendColors(a: vec3<f32>, b: vec3<f32>, t: f32) -> vec3<f32> {
    return mix(a, b, t);
  }
`);

material.colorNode = blendColors(colorA, colorB, blendFactor);
```

### Advanced Math Functions

```javascript
const fresnelSchlick = wgslFn(`
  fn fresnelSchlick(cosTheta: f32, F0: vec3<f32>) -> vec3<f32> {
    return F0 + (vec3<f32>(1.0) - F0) * pow(1.0 - cosTheta, 5.0);
  }
`);

const GGX = wgslFn(`
  fn distributionGGX(N: vec3<f32>, H: vec3<f32>, roughness: f32) -> f32 {
    let a = roughness * roughness;
    let a2 = a * a;
    let NdotH = max(dot(N, H), 0.0);
    let NdotH2 = NdotH * NdotH;

    let num = a2;
    let denom = (NdotH2 * (a2 - 1.0) + 1.0);
    denom = 3.14159265359 * denom * denom;

    return num / denom;
  }
`);
```

### Noise Functions

```javascript
const simplexNoise = wgslFn(`
  fn mod289(x: vec3<f32>) -> vec3<f32> {
    return x - floor(x * (1.0 / 289.0)) * 289.0;
  }

  fn permute(x: vec3<f32>) -> vec3<f32> {
    return mod289(((x * 34.0) + 1.0) * x);
  }

  fn snoise(v: vec2<f32>) -> f32 {
    let C = vec4<f32>(
      0.211324865405187,
      0.366025403784439,
      -0.577350269189626,
      0.024390243902439
    );

    var i = floor(v + dot(v, C.yy));
    let x0 = v - i + dot(i, C.xx);

    var i1: vec2<f32>;
    if (x0.x > x0.y) {
      i1 = vec2<f32>(1.0, 0.0);
    } else {
      i1 = vec2<f32>(0.0, 1.0);
    }

    var x12 = x0.xyxy + C.xxzz;
    x12 = vec4<f32>(x12.xy - i1, x12.zw);

    i = mod289(vec3<f32>(i, 0.0)).xy;
    let p = permute(permute(i.y + vec3<f32>(0.0, i1.y, 1.0)) + i.x + vec3<f32>(0.0, i1.x, 1.0));

    var m = max(vec3<f32>(0.5) - vec3<f32>(dot(x0, x0), dot(x12.xy, x12.xy), dot(x12.zw, x12.zw)), vec3<f32>(0.0));
    m = m * m;
    m = m * m;

    let x = 2.0 * fract(p * C.www) - 1.0;
    let h = abs(x) - 0.5;
    let ox = floor(x + 0.5);
    let a0 = x - ox;

    m = m * (1.79284291400159 - 0.85373472095314 * (a0 * a0 + h * h));

    let g = vec3<f32>(
      a0.x * x0.x + h.x * x0.y,
      a0.y * x12.x + h.y * x12.y,
      a0.z * x12.z + h.z * x12.w
    );

    return 130.0 * dot(m, g);
  }
`);

// Use noise
const noiseValue = simplexNoise(uv().mul(10.0));
```

### FBM (Fractal Brownian Motion)

```javascript
const fbm = wgslFn(`
  fn fbm(p: vec2<f32>, octaves: i32) -> f32 {
    var value = 0.0;
    var amplitude = 0.5;
    var frequency = 1.0;
    var pos = p;

    for (var i = 0; i < octaves; i = i + 1) {
      value = value + amplitude * snoise(pos * frequency);
      amplitude = amplitude * 0.5;
      frequency = frequency * 2.0;
    }

    return value;
  }
`);
```

## WGSL Types Reference

### Scalar Types
```wgsl
bool        // Boolean
i32         // 32-bit signed integer
u32         // 32-bit unsigned integer
f32         // 32-bit float
f16         // 16-bit float (if enabled)
```

### Vector Types
```wgsl
vec2<f32>   // 2D float vector
vec3<f32>   // 3D float vector
vec4<f32>   // 4D float vector
vec2<i32>   // 2D integer vector
vec2<u32>   // 2D unsigned integer vector
```

### Matrix Types
```wgsl
mat2x2<f32> // 2x2 matrix
mat3x3<f32> // 3x3 matrix
mat4x4<f32> // 4x4 matrix
mat2x3<f32> // 2 columns, 3 rows
```

### Texture Types
```wgsl
texture_2d<f32>
texture_3d<f32>
texture_cube<f32>
texture_storage_2d<rgba8unorm, write>
```

## WGSL Syntax Reference

### Variables
```wgsl
let x = 1.0;              // Immutable
var y = 2.0;              // Mutable
const PI = 3.14159;       // Compile-time constant
```

### Control Flow
```wgsl
// If-else
if (condition) {
  // ...
} else if (other) {
  // ...
} else {
  // ...
}

// For loop
for (var i = 0; i < 10; i = i + 1) {
  // ...
}

// While loop
while (condition) {
  // ...
}

// Switch
switch (value) {
  case 0: { /* ... */ }
  case 1, 2: { /* ... */ }
  default: { /* ... */ }
}
```

### Built-in Functions
```wgsl
// Math
abs(x), sign(x), floor(x), ceil(x), round(x)
fract(x), trunc(x)
min(a, b), max(a, b), clamp(x, lo, hi)
mix(a, b, t), step(edge, x), smoothstep(lo, hi, x)
sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), atan2(y, x)
pow(x, y), exp(x), log(x), exp2(x), log2(x)
sqrt(x), inverseSqrt(x)

// Vector
length(v), distance(a, b)
dot(a, b), cross(a, b)
normalize(v), faceForward(n, i, nref)
reflect(i, n), refract(i, n, eta)

// Matrix
transpose(m), determinant(m)

// Texture
textureSample(t, s, coord)
textureLoad(t, coord, level)
textureStore(t, coord, value)
textureDimensions(t)
```

## Combining TSL and WGSL

### TSL Wrapper for WGSL

```javascript
import { Fn, wgslFn, float, vec2, vec3 } from 'three/tsl';

// WGSL implementation
const wgslNoise = wgslFn(`
  fn noise2d(p: vec2<f32>) -> f32 {
    return fract(sin(dot(p, vec2<f32>(12.9898, 78.233))) * 43758.5453);
  }
`);

// TSL wrapper with nice API
const noise = Fn(([position, scale = 1.0]) => {
  return wgslNoise(position.xy.mul(scale));
});

// Use
material.colorNode = vec3(noise(positionWorld, 10.0));
```

### Hybrid Approach

```javascript
// Complex math in WGSL
const complexMath = wgslFn(`
  fn complexOperation(a: vec3<f32>, b: vec3<f32>, t: f32) -> vec3<f32> {
    let blended = mix(a, b, t);
    let rotated = vec3<f32>(
      blended.x * cos(t) - blended.y * sin(t),
      blended.x * sin(t) + blended.y * cos(t),
      blended.z
    );
    return normalize(rotated);
  }
`);

// Simple logic in TSL
const finalColor = Fn(() => {
  const base = texture(diffuseMap).rgb;
  const processed = complexMath(base, vec3(1, 0, 0), time);
  return mix(base, processed, oscSine(time));
});

material.colorNode = finalColor();
```

## Performance Tips

### Avoid Branching When Possible
```wgsl
// Instead of:
if (x > 0.5) {
  result = a;
} else {
  result = b;
}

// Use:
result = mix(b, a, step(0.5, x));
```

### Use Local Variables
```wgsl
fn compute(p: vec2<f32>) -> f32 {
  // Cache repeated calculations
  let p2 = p * p;
  let p4 = p2 * p2;
  return p2.x + p2.y + p4.x * p4.y;
}
```

### Minimize Texture Samples
```wgsl
// Sample once, use multiple times
let sample = textureSample(tex, sampler, uv);
let r = sample.r;
let g = sample.g;
let b = sample.b;
```
```

## File: `skills/webgpu-threejs-tsl/examples/basic-setup.js`
```javascript
/**
 * Basic WebGPU Three.js Setup
 *
 * Minimal example showing WebGPU renderer initialization
 * with a simple animated mesh using TSL.
 *
 * Based on Three.js examples (MIT License)
 * https://github.com/mrdoob/three.js
 */

import * as THREE from 'three/webgpu';
import { color, time, oscSine, positionLocal, normalWorld } from 'three/tsl';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

let camera, scene, renderer, controls;

async function init() {
  // Camera
  camera = new THREE.PerspectiveCamera(
    70,
    window.innerWidth / window.innerHeight,
    0.1,
    100
  );
  camera.position.z = 4;

  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x111111);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0x404040);
  scene.add(ambientLight);

  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(5, 5, 5);
  scene.add(directionalLight);

  // Create mesh with TSL material
  const geometry = new THREE.TorusKnotGeometry(1, 0.3, 128, 32);
  const material = new THREE.MeshStandardNodeMaterial();

  // Animated color using TSL
  material.colorNode = color(0x0088ff).mul(
    oscSine(time.mul(0.5)).mul(0.5).add(0.5)
  );

  // Add slight position wobble
  material.positionNode = positionLocal.add(
    normalWorld.mul(oscSine(time.mul(2.0).add(positionLocal.y)).mul(0.05))
  );

  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  // Renderer
  renderer = new THREE.WebGPURenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  document.body.appendChild(renderer.domElement);

  // Initialize WebGPU
  await renderer.init();

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;

  // Handle resize
  window.addEventListener('resize', onWindowResize);

  // Start animation loop
  renderer.setAnimationLoop(animate);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
  controls.update();
  renderer.render(scene, camera);
}

init();
```

## File: `skills/webgpu-threejs-tsl/examples/custom-material.js`
```javascript
/**
 * Custom TSL Material Example
 *
 * Demonstrates creating custom shader effects using TSL:
 * - Fresnel rim lighting
 * - Animated patterns
 * - Dynamic displacement
 *
 * Based on Three.js examples (MIT License)
 * https://github.com/mrdoob/three.js
 */

import * as THREE from 'three/webgpu';
import {
  Fn,
  color,
  float,
  vec2,
  vec3,
  uniform,
  texture,
  uv,
  time,
  mix,
  smoothstep,
  sin,
  cos,
  positionLocal,
  positionWorld,
  normalLocal,
  normalWorld,
  cameraPosition
} from 'three/tsl';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

let camera, scene, renderer, controls;
let rimColor, patternScale, displacementStrength;

async function init() {
  // Setup
  camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.z = 3;

  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x000000);

  // Uniforms for runtime control
  rimColor = uniform(new THREE.Color(0x00ffff));
  patternScale = uniform(5.0);
  displacementStrength = uniform(0.1);

  // Create custom material
  const material = createCustomMaterial();

  // Mesh
  const geometry = new THREE.IcosahedronGeometry(1, 64);
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  // Renderer
  renderer = new THREE.WebGPURenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  document.body.appendChild(renderer.domElement);
  await renderer.init();

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;

  // Events
  window.addEventListener('resize', onWindowResize);

  // GUI (optional - requires lil-gui)
  setupGUI();

  renderer.setAnimationLoop(animate);
}

function createCustomMaterial() {
  const material = new THREE.MeshStandardNodeMaterial();

  // --- Fresnel Rim Effect ---
  const fresnel = Fn(() => {
    const viewDir = cameraPosition.sub(positionWorld).normalize();
    const nDotV = normalWorld.dot(viewDir).saturate();
    return float(1.0).sub(nDotV).pow(3.0);
  });

  // --- Animated Pattern ---
  const animatedPattern = Fn(() => {
    const uvCoord = uv().mul(patternScale);
    const t = time.mul(0.5);

    // Create animated wave pattern
    const wave1 = sin(uvCoord.x.mul(10.0).add(t)).mul(0.5).add(0.5);
    const wave2 = sin(uvCoord.y.mul(10.0).sub(t.mul(1.3))).mul(0.5).add(0.5);
    const wave3 = sin(uvCoord.x.add(uvCoord.y).mul(7.0).add(t.mul(0.7))).mul(0.5).add(0.5);

    return wave1.mul(wave2).mul(wave3);
  });

  // --- Displacement ---
  const displacement = Fn(() => {
    const pattern = animatedPattern();
    return normalLocal.mul(pattern.mul(displacementStrength));
  });

  // Apply displacement
  material.positionNode = positionLocal.add(displacement());

  // --- Color ---
  const baseColor = color(0x222244);
  const highlightColor = color(0x4444ff);

  // Mix colors based on pattern
  const pattern = animatedPattern();
  const surfaceColor = mix(baseColor, highlightColor, pattern);

  material.colorNode = surfaceColor;

  // --- Rim lighting ---
  material.emissiveNode = rimColor.mul(fresnel());

  // --- PBR properties ---
  material.roughnessNode = float(0.3).add(pattern.mul(0.4));
  material.metalnessNode = float(0.1);

  return material;
}

function setupGUI() {
  // Only setup if lil-gui is available
  if (typeof window.GUI === 'undefined') {
    console.log('Add lil-gui for interactive controls');
    return;
  }

  const gui = new GUI();
  const params = {
    rimColor: '#00ffff',
    patternScale: 5.0,
    displacementStrength: 0.1
  };

  gui.addColor(params, 'rimColor').onChange((value) => {
    rimColor.value.set(value);
  });

  gui.add(params, 'patternScale', 1, 20).onChange((value) => {
    patternScale.value = value;
  });

  gui.add(params, 'displacementStrength', 0, 0.5).onChange((value) => {
    displacementStrength.value = value;
  });
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
  controls.update();
  renderer.render(scene, camera);
}

init();
```

## File: `skills/webgpu-threejs-tsl/examples/earth-shader.js`
```javascript
/**
 * Earth Shader Example
 *
 * Complete procedural Earth with:
 * - Day/night texture blending
 * - Atmospheric glow (fresnel)
 * - Cloud layer
 * - City lights at night
 * - Bump mapping
 *
 * Based on Three.js webgpu_tsl_earth example (MIT License)
 * https://github.com/mrdoob/three.js
 */

import * as THREE from 'three/webgpu';
import {
  Fn,
  If,
  float,
  vec2,
  vec3,
  vec4,
  color,
  uniform,
  texture,
  uv,
  time,
  mix,
  smoothstep,
  pow,
  clamp,
  normalize,
  dot,
  max,
  positionWorld,
  normalWorld,
  normalLocal,
  cameraPosition,
  bumpMap
} from 'three/tsl';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

let camera, scene, renderer, controls;
let earth, clouds, atmosphere;

// Uniforms
const sunDirection = uniform(new THREE.Vector3(1, 0.2, 0.5).normalize());
const atmosphereDayColor = uniform(new THREE.Color(0x4db2ff));
const atmosphereTwilightColor = uniform(new THREE.Color(0xbd5f1b));
const cloudSpeed = uniform(0.01);
const cityLightIntensity = uniform(1.5);

async function init() {
  // Camera
  camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.set(0, 0, 4);

  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x000011);

  // Load textures
  const loader = new THREE.TextureLoader();

  // Note: Replace with actual texture paths
  const earthDayTexture = loader.load('textures/earth_day.jpg');
  const earthNightTexture = loader.load('textures/earth_night.jpg');
  const earthCloudsTexture = loader.load('textures/earth_clouds.jpg');
  const earthBumpTexture = loader.load('textures/earth_bump.jpg');

  // Set texture properties
  [earthDayTexture, earthNightTexture, earthCloudsTexture, earthBumpTexture].forEach((tex) => {
    tex.colorSpace = THREE.SRGBColorSpace;
    tex.wrapS = THREE.RepeatWrapping;
    tex.wrapT = THREE.ClampToEdgeWrapping;
  });

  // Create Earth
  earth = createEarth(earthDayTexture, earthNightTexture, earthBumpTexture);
  scene.add(earth);

  // Create cloud layer
  clouds = createClouds(earthCloudsTexture);
  scene.add(clouds);

  // Create atmosphere glow
  atmosphere = createAtmosphere();
  scene.add(atmosphere);

  // Stars background
  createStars();

  // Renderer
  renderer = new THREE.WebGPURenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  document.body.appendChild(renderer.domElement);
  await renderer.init();

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.minDistance = 2;
  controls.maxDistance = 10;

  // Events
  window.addEventListener('resize', onWindowResize);

  renderer.setAnimationLoop(animate);
}

function createEarth(dayTex, nightTex, bumpTex) {
  const geometry = new THREE.SphereGeometry(1, 64, 64);
  const material = new THREE.MeshStandardNodeMaterial();

  // Sun illumination factor
  const sunOrientation = Fn(() => {
    return normalWorld.dot(sunDirection).mul(0.5).add(0.5);
  });

  // Day/night color mixing
  material.colorNode = Fn(() => {
    const dayColor = texture(dayTex, uv());
    const nightColor = texture(nightTex, uv());

    const orientation = sunOrientation();
    const dayNight = smoothstep(0.4, 0.6, orientation);

    // Add city lights on night side
    const cityLights = nightColor.mul(cityLightIntensity).mul(
      float(1.0).sub(dayNight)
    );

    const baseColor = mix(nightColor, dayColor, dayNight);
    return baseColor.add(cityLights.mul(float(1.0).sub(orientation).pow(2.0)));
  })();

  // Bump mapping for terrain
  material.normalNode = bumpMap(texture(bumpTex, uv()), 0.03);

  // PBR properties vary with day/night
  material.roughnessNode = Fn(() => {
    const orientation = sunOrientation();
    return mix(float(0.8), float(0.4), smoothstep(0.3, 0.7, orientation));
  })();

  material.metalnessNode = float(0.0);

  // Subtle atmospheric rim on day side
  material.emissiveNode = Fn(() => {
    const viewDir = normalize(cameraPosition.sub(positionWorld));
    const fresnel = pow(float(1.0).sub(normalWorld.dot(viewDir).saturate()), 4.0);

    const orientation = sunOrientation();
    const atmosphereColor = mix(atmosphereTwilightColor, atmosphereDayColor, orientation);

    return atmosphereColor.mul(fresnel).mul(orientation).mul(0.3);
  })();

  return new THREE.Mesh(geometry, material);
}

function createClouds(cloudsTex) {
  const geometry = new THREE.SphereGeometry(1.01, 64, 64);
  const material = new THREE.MeshStandardNodeMaterial();

  // Animated UV for cloud movement
  const cloudUV = Fn(() => {
    const baseUV = uv();
    const offset = time.mul(cloudSpeed);
    return vec2(baseUV.x.add(offset), baseUV.y);
  });

  // Cloud color (white with transparency)
  material.colorNode = color(0xffffff);

  // Cloud opacity from texture
  material.opacityNode = Fn(() => {
    const cloudAlpha = texture(cloudsTex, cloudUV()).r;

    // Fade clouds on night side
    const sunOrientation = normalWorld.dot(sunDirection).mul(0.5).add(0.5);
    const dayFactor = smoothstep(0.2, 0.5, sunOrientation);

    return cloudAlpha.mul(0.8).mul(dayFactor.mul(0.5).add(0.5));
  })();

  material.transparent = true;
  material.depthWrite = false;
  material.side = THREE.DoubleSide;

  // Slight self-illumination
  material.emissiveNode = Fn(() => {
    const sunOrientation = normalWorld.dot(sunDirection).mul(0.5).add(0.5);
    return color(0xffffff).mul(sunOrientation.mul(0.1));
  })();

  return new THREE.Mesh(geometry, material);
}

function createAtmosphere() {
  const geometry = new THREE.SphereGeometry(1.15, 64, 64);
  const material = new THREE.MeshBasicNodeMaterial();

  material.colorNode = Fn(() => {
    const viewDir = normalize(cameraPosition.sub(positionWorld));
    const fresnel = pow(float(1.0).sub(normalWorld.dot(viewDir).abs()), 3.0);

    const sunOrientation = normalWorld.dot(sunDirection).mul(0.5).add(0.5);
    const atmosphereColor = mix(atmosphereTwilightColor, atmosphereDayColor, sunOrientation);

    return atmosphereColor;
  })();

  material.opacityNode = Fn(() => {
    const viewDir = normalize(cameraPosition.sub(positionWorld));
    const fresnel = pow(float(1.0).sub(normalWorld.dot(viewDir).abs()), 2.5);

    // Stronger on day side
    const sunOrientation = normalWorld.dot(sunDirection).mul(0.5).add(0.5);

    return fresnel.mul(sunOrientation.mul(0.5).add(0.3));
  })();

  material.transparent = true;
  material.depthWrite = false;
  material.side = THREE.BackSide;

  return new THREE.Mesh(geometry, material);
}

function createStars() {
  const starsGeometry = new THREE.BufferGeometry();
  const starCount = 2000;

  const positions = new Float32Array(starCount * 3);
  const colors = new Float32Array(starCount * 3);

  for (let i = 0; i < starCount; i++) {
    // Random position on sphere
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(Math.random() * 2 - 1);
    const radius = 50 + Math.random() * 50;

    positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
    positions[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
    positions[i * 3 + 2] = radius * Math.cos(phi);

    // Slight color variation
    const brightness = 0.5 + Math.random() * 0.5;
    colors[i * 3] = brightness;
    colors[i * 3 + 1] = brightness;
    colors[i * 3 + 2] = brightness + Math.random() * 0.2;
  }

  starsGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  starsGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  const starsMaterial = new THREE.PointsNodeMaterial();
  starsMaterial.colorNode = Fn(() => {
    return vec3(1.0);
  })();
  starsMaterial.sizeNode = float(2.0);
  starsMaterial.vertexColors = true;

  const stars = new THREE.Points(starsGeometry, starsMaterial);
  scene.add(stars);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
  // Rotate Earth slowly
  earth.rotation.y += 0.001;
  clouds.rotation.y += 0.0012;

  // Animate sun direction (optional - creates day/night cycle)
  // const angle = time.value * 0.1;
  // sunDirection.value.set(Math.cos(angle), 0.2, Math.sin(angle)).normalize();

  controls.update();
  renderer.render(scene, camera);
}

init();

// Export for external control
export { sunDirection, atmosphereDayColor, atmosphereTwilightColor, cloudSpeed, cityLightIntensity };
```

## File: `skills/webgpu-threejs-tsl/examples/particle-system.js`
```javascript
/**
 * GPU Particle System with Compute Shaders
 *
 * Demonstrates TSL compute shaders for particle simulation:
 * - Instanced array buffers
 * - Physics simulation on GPU
 * - Mouse interaction
 *
 * Based on Three.js webgpu_compute_particles example (MIT License)
 * https://github.com/mrdoob/three.js
 */

import * as THREE from 'three/webgpu';
import {
  Fn,
  If,
  uniform,
  float,
  vec3,
  color,
  instancedArray,
  instanceIndex,
  hash,
  time
} from 'three/tsl';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

let camera, scene, renderer, controls;
let computeInit, computeUpdate, computeHit;

// Particle count
const PARTICLE_COUNT = 100000;

// Storage buffers
const positions = instancedArray(PARTICLE_COUNT, 'vec3');
const velocities = instancedArray(PARTICLE_COUNT, 'vec3');

// Uniforms
const gravity = uniform(-9.8);
const bounce = uniform(0.7);
const friction = uniform(0.98);
const deltaTimeUniform = uniform(0);
const clickPosition = uniform(new THREE.Vector3());
const hitStrength = uniform(5.0);

async function init() {
  // Camera
  camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.set(0, 5, 15);

  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x111122);

  // Create compute shaders
  createComputeShaders();

  // Create particle mesh
  createParticleMesh();

  // Floor
  const floorGeometry = new THREE.PlaneGeometry(30, 30);
  const floorMaterial = new THREE.MeshStandardNodeMaterial({
    color: 0x333333
  });
  const floor = new THREE.Mesh(floorGeometry, floorMaterial);
  floor.rotation.x = -Math.PI / 2;
  floor.receiveShadow = true;
  scene.add(floor);

  // Lights
  const ambientLight = new THREE.AmbientLight(0x404040);
  scene.add(ambientLight);

  const pointLight = new THREE.PointLight(0xffffff, 100);
  pointLight.position.set(5, 10, 5);
  scene.add(pointLight);

  // Renderer
  renderer = new THREE.WebGPURenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  document.body.appendChild(renderer.domElement);
  await renderer.init();

  // Initialize particles
  await renderer.computeAsync(computeInit);

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.target.set(0, 2, 0);

  // Events
  window.addEventListener('resize', onWindowResize);
  renderer.domElement.addEventListener('click', onClick);

  renderer.setAnimationLoop(animate);
}

function createComputeShaders() {
  // Grid dimensions for initialization
  const gridSize = Math.ceil(Math.sqrt(PARTICLE_COUNT));
  const spacing = 0.15;
  const offset = (gridSize * spacing) / 2;

  // Initialize particles in a grid
  computeInit = Fn(() => {
    const position = positions.element(instanceIndex);
    const velocity = velocities.element(instanceIndex);

    // Calculate grid position
    const x = instanceIndex.mod(gridSize);
    const z = instanceIndex.div(gridSize);

    // Set position
    position.x.assign(x.toFloat().mul(spacing).sub(offset));
    position.y.assign(float(5.0).add(hash(instanceIndex).mul(2.0)));
    position.z.assign(z.toFloat().mul(spacing).sub(offset));

    // Random initial velocity
    velocity.x.assign(hash(instanceIndex.add(1)).sub(0.5).mul(2.0));
    velocity.y.assign(hash(instanceIndex.add(2)).mul(-2.0));
    velocity.z.assign(hash(instanceIndex.add(3)).sub(0.5).mul(2.0));
  })().compute(PARTICLE_COUNT);

  // Physics update
  computeUpdate = Fn(() => {
    const position = positions.element(instanceIndex);
    const velocity = velocities.element(instanceIndex);
    const dt = deltaTimeUniform;

    // Apply gravity
    velocity.y.addAssign(gravity.mul(dt));

    // Update position
    position.addAssign(velocity.mul(dt));

    // Apply friction
    velocity.mulAssign(friction);

    // Ground collision
    If(position.y.lessThan(0), () => {
      position.y.assign(0);
      velocity.y.assign(velocity.y.abs().mul(bounce)); // Reverse and dampen

      // Extra friction on ground
      velocity.x.mulAssign(0.9);
      velocity.z.mulAssign(0.9);
    });

    // Boundary walls
    If(position.x.abs().greaterThan(15), () => {
      position.x.assign(position.x.sign().mul(15));
      velocity.x.assign(velocity.x.negate().mul(bounce));
    });

    If(position.z.abs().greaterThan(15), () => {
      position.z.assign(position.z.sign().mul(15));
      velocity.z.assign(velocity.z.negate().mul(bounce));
    });
  })().compute(PARTICLE_COUNT);

  // Hit/explosion effect
  computeHit = Fn(() => {
    const position = positions.element(instanceIndex);
    const velocity = velocities.element(instanceIndex);

    // Distance to click
    const toClick = position.sub(clickPosition);
    const distance = toClick.length();

    // Apply force within radius
    If(distance.lessThan(3.0), () => {
      const direction = toClick.normalize();
      const force = float(3.0).sub(distance).div(3.0).mul(hitStrength);

      // Add randomness
      const randomForce = force.mul(hash(instanceIndex.add(time.mul(1000))).mul(0.5).add(0.75));

      velocity.addAssign(direction.mul(randomForce));
      velocity.y.addAssign(randomForce.mul(0.5));
    });
  })().compute(PARTICLE_COUNT);
}

function createParticleMesh() {
  // Simple sphere geometry for each particle
  const geometry = new THREE.SphereGeometry(0.08, 8, 8);

  // Material using computed positions
  const material = new THREE.MeshStandardNodeMaterial();

  // Position from compute buffer
  material.positionNode = positions.element(instanceIndex);

  // Color based on velocity
  material.colorNode = Fn(() => {
    const velocity = velocities.element(instanceIndex);
    const speed = velocity.length();

    // Color gradient: blue (slow) -> orange (fast)
    const t = speed.div(10.0).saturate();
    return color(0x0066ff).mix(color(0xff6600), t);
  })();

  material.roughnessNode = float(0.5);
  material.metalnessNode = float(0.2);

  // Create instanced mesh
  const mesh = new THREE.InstancedMesh(geometry, material, PARTICLE_COUNT);
  scene.add(mesh);
}

function onClick(event) {
  // Raycast to find click position on floor
  const raycaster = new THREE.Raycaster();
  const mouse = new THREE.Vector2(
    (event.clientX / window.innerWidth) * 2 - 1,
    -(event.clientY / window.innerHeight) * 2 + 1
  );

  raycaster.setFromCamera(mouse, camera);

  // Intersect with floor plane (y = 0)
  const plane = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0);
  const intersection = new THREE.Vector3();
  raycaster.ray.intersectPlane(plane, intersection);

  if (intersection) {
    // Raise click position slightly
    intersection.y = 0.5;
    clickPosition.value.copy(intersection);

    // Run hit compute shader
    renderer.compute(computeHit);
  }
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

const clock = new THREE.Clock();

function animate() {
  // Update delta time
  deltaTimeUniform.value = Math.min(clock.getDelta(), 0.1);

  // Run physics compute
  renderer.compute(computeUpdate);

  controls.update();
  renderer.render(scene, camera);
}

init();
```

## File: `skills/webgpu-threejs-tsl/examples/post-processing.js`
```javascript
/**
 * Post-Processing Pipeline Example
 *
 * Demonstrates TSL post-processing:
 * - Bloom effect
 * - Custom vignette
 * - Color grading
 * - Effect chaining
 *
 * Based on Three.js webgpu_postprocessing examples (MIT License)
 * https://github.com/mrdoob/three.js
 */

import * as THREE from 'three/webgpu';
import {
  Fn,
  float,
  vec2,
  vec3,
  vec4,
  color,
  uniform,
  pass,
  screenUV,
  screenSize,
  time,
  oscSine,
  mix,
  smoothstep,
  texture,
  grayscale,
  saturation
} from 'three/tsl';
import { bloom } from 'three/addons/tsl/display/BloomNode.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

let camera, scene, renderer, controls;
let postProcessing;

// Effect uniforms
const bloomStrength = uniform(1.0);
const bloomThreshold = uniform(0.5);
const vignetteIntensity = uniform(0.5);
const saturationAmount = uniform(1.2);
const colorTint = uniform(new THREE.Color(1.0, 0.95, 0.9));

async function init() {
  // Camera
  camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.set(0, 2, 8);

  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x111111);

  // Add objects with emissive materials (for bloom)
  createScene();

  // Renderer
  renderer = new THREE.WebGPURenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  document.body.appendChild(renderer.domElement);
  await renderer.init();

  // Create post-processing pipeline
  setupPostProcessing();

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.target.set(0, 1, 0);

  // Events
  window.addEventListener('resize', onWindowResize);

  renderer.setAnimationLoop(animate);
}

function createScene() {
  // Floor
  const floorGeometry = new THREE.PlaneGeometry(20, 20);
  const floorMaterial = new THREE.MeshStandardNodeMaterial({
    color: 0x222222
  });
  const floor = new THREE.Mesh(floorGeometry, floorMaterial);
  floor.rotation.x = -Math.PI / 2;
  scene.add(floor);

  // Emissive spheres (will bloom)
  const sphereGeometry = new THREE.SphereGeometry(0.5, 32, 32);

  const colors = [0xff0044, 0x00ff88, 0x4488ff, 0xffaa00, 0xff00ff];

  for (let i = 0; i < 5; i++) {
    const material = new THREE.MeshStandardNodeMaterial();

    // Base color
    material.colorNode = color(colors[i]).mul(0.3);

    // Animated emissive
    material.emissiveNode = Fn(() => {
      const pulse = oscSine(time.mul(1.0 + i * 0.2)).mul(0.5).add(0.5);
      return color(colors[i]).mul(pulse.mul(2.0).add(0.5));
    })();

    material.roughnessNode = float(0.2);
    material.metalnessNode = float(0.8);

    const sphere = new THREE.Mesh(sphereGeometry, material);
    sphere.position.set(
      Math.cos((i / 5) * Math.PI * 2) * 3,
      1 + Math.sin(i) * 0.5,
      Math.sin((i / 5) * Math.PI * 2) * 3
    );
    scene.add(sphere);
  }

  // Central reflective sphere
  const centerMaterial = new THREE.MeshStandardNodeMaterial();
  centerMaterial.colorNode = color(0x888888);
  centerMaterial.roughnessNode = float(0.1);
  centerMaterial.metalnessNode = float(1.0);

  const centerSphere = new THREE.Mesh(new THREE.SphereGeometry(1, 64, 64), centerMaterial);
  centerSphere.position.y = 1;
  scene.add(centerSphere);

  // Lights
  const ambientLight = new THREE.AmbientLight(0x404040, 0.5);
  scene.add(ambientLight);

  const pointLight = new THREE.PointLight(0xffffff, 50);
  pointLight.position.set(5, 10, 5);
  scene.add(pointLight);
}

function setupPostProcessing() {
  // Create post-processing instance
  postProcessing = new THREE.PostProcessing(renderer);

  // Create scene pass
  const scenePass = pass(scene, camera);
  const sceneColor = scenePass.getTextureNode('output');

  // --- Effect Chain ---

  // 1. Bloom
  const bloomPass = bloom(sceneColor);
  bloomPass.threshold = bloomThreshold;
  bloomPass.strength = bloomStrength;
  bloomPass.radius = uniform(0.5);

  // Add bloom to scene
  let output = sceneColor.add(bloomPass);

  // 2. Color Grading
  output = saturation(output, saturationAmount);
  output = output.mul(colorTint);

  // 3. Vignette (custom effect)
  const vignette = Fn(() => {
    const uv = screenUV;
    const dist = uv.sub(0.5).length();
    return float(1.0).sub(dist.mul(vignetteIntensity).pow(2.0)).saturate();
  });

  output = output.mul(vignette());

  // 4. Optional: Scanlines
  const scanlines = Fn(() => {
    const scanline = screenUV.y.mul(screenSize.y).mul(0.5).sin().mul(0.05).add(0.95);
    return scanline;
  });

  // Uncomment for CRT effect:
  // output = output.mul(scanlines());

  // Set final output
  postProcessing.outputNode = output;
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
  controls.update();

  // Render with post-processing
  postProcessing.render();
}

init();

// Export uniforms for external control (e.g., GUI)
export { bloomStrength, bloomThreshold, vignetteIntensity, saturationAmount, colorTint };
```

## File: `skills/webgpu-threejs-tsl/templates/compute-shader.js`
```javascript
/**
 * Compute Shader Template
 *
 * A template for GPU compute shaders with:
 * - Storage buffer setup
 * - Initialize and update shaders
 * - Visualization with instanced mesh
 *
 * Usage:
 * 1. Modify PARTICLE_COUNT and buffer types
 * 2. Implement your initialization logic
 * 3. Implement your update logic
 * 4. Customize visualization
 */

import * as THREE from 'three/webgpu';
import {
  Fn,
  If,
  Loop,
  float,
  int,
  vec2,
  vec3,
  vec4,
  color,
  uniform,
  instancedArray,
  instanceIndex,
  hash,
  time,
  deltaTime
} from 'three/tsl';

import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// ============================================
// CONFIGURATION
// ============================================

const PARTICLE_COUNT = 50000;

// ============================================
// STORAGE BUFFERS
// ============================================

// Define your storage buffers here
// Available types: 'float', 'vec2', 'vec3', 'vec4', 'int', 'uint'

const positions = instancedArray(PARTICLE_COUNT, 'vec3');
const velocities = instancedArray(PARTICLE_COUNT, 'vec3');
// Add more buffers as needed:
// const colors = instancedArray(PARTICLE_COUNT, 'vec3');
// const lifetimes = instancedArray(PARTICLE_COUNT, 'float');
// const states = instancedArray(PARTICLE_COUNT, 'uint');

// ============================================
// UNIFORMS
// ============================================

const dt = uniform(0);
// Add your uniforms here:
// const gravity = uniform(-9.8);
// const attractorPosition = uniform(new THREE.Vector3());
// const forceStrength = uniform(1.0);

// ============================================
// COMPUTE SHADERS
// ============================================

/**
 * Initialize particles
 * Called once at startup
 */
const computeInit = Fn(() => {
  const position = positions.element(instanceIndex);
  const velocity = velocities.element(instanceIndex);

  // ========================================
  // IMPLEMENT YOUR INITIALIZATION HERE
  // ========================================

  // Example: Random positions in a cube
  position.x.assign(hash(instanceIndex).sub(0.5).mul(10));
  position.y.assign(hash(instanceIndex.add(1)).sub(0.5).mul(10));
  position.z.assign(hash(instanceIndex.add(2)).sub(0.5).mul(10));

  // Example: Zero velocity
  velocity.assign(vec3(0));
})().compute(PARTICLE_COUNT);

/**
 * Update particles each frame
 * Called every frame in animation loop
 */
const computeUpdate = Fn(() => {
  const position = positions.element(instanceIndex);
  const velocity = velocities.element(instanceIndex);

  // ========================================
  // IMPLEMENT YOUR UPDATE LOGIC HERE
  // ========================================

  // Example: Simple gravity
  velocity.y.addAssign(float(-9.8).mul(dt));

  // Example: Update position
  position.addAssign(velocity.mul(dt));

  // Example: Ground bounce
  If(position.y.lessThan(0), () => {
    position.y.assign(0);
    velocity.y.assign(velocity.y.negate().mul(0.8));
  });

  // Example: Boundary wrapping
  // If(position.x.abs().greaterThan(5), () => {
  //   position.x.assign(position.x.negate());
  // });
})().compute(PARTICLE_COUNT);

/**
 * Optional: Additional compute pass (e.g., for interactions)
 */
const computeInteraction = Fn(() => {
  const position = positions.element(instanceIndex);
  const velocity = velocities.element(instanceIndex);

  // ========================================
  // IMPLEMENT INTERACTION LOGIC HERE
  // ========================================

  // Example: Attract to point
  // const toTarget = attractorPosition.sub(position);
  // const dist = toTarget.length();
  // const force = toTarget.normalize().mul(forceStrength).div(dist.add(0.1));
  // velocity.addAssign(force.mul(dt));
})().compute(PARTICLE_COUNT);

// ============================================
// VISUALIZATION
// ============================================

function createVisualization(scene) {
  // Choose visualization type:
  // - Points (fastest, simplest)
  // - Instanced Mesh (more control)

  // Option 1: Points
  // return createPointsVisualization(scene);

  // Option 2: Instanced Mesh
  return createInstancedVisualization(scene);
}

function createPointsVisualization(scene) {
  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute(
    'position',
    new THREE.Float32BufferAttribute(new Float32Array(PARTICLE_COUNT * 3), 3)
  );

  const material = new THREE.PointsNodeMaterial();

  // Position from compute buffer
  material.positionNode = positions.element(instanceIndex);

  // ========================================
  // CUSTOMIZE POINT APPEARANCE HERE
  // ========================================

  material.sizeNode = float(3.0);

  material.colorNode = Fn(() => {
    // Example: Color based on velocity
    const velocity = velocities.element(instanceIndex);
    const speed = velocity.length();
    return mix(color(0x0066ff), color(0xff6600), speed.div(5).saturate());
  })();

  const points = new THREE.Points(geometry, material);
  scene.add(points);
  return points;
}

function createInstancedVisualization(scene) {
  // Geometry for each instance
  const geometry = new THREE.SphereGeometry(0.05, 8, 8);
  // Or use simpler geometry for better performance:
  // const geometry = new THREE.IcosahedronGeometry(0.05, 0);

  const material = new THREE.MeshStandardNodeMaterial();

  // Position from compute buffer
  material.positionNode = positions.element(instanceIndex);

  // ========================================
  // CUSTOMIZE MESH APPEARANCE HERE
  // ========================================

  material.colorNode = Fn(() => {
    // Example: Color based on position
    const position = positions.element(instanceIndex);
    return color(0x0088ff).add(position.mul(0.05));
  })();

  material.roughnessNode = float(0.5);
  material.metalnessNode = float(0.2);

  const mesh = new THREE.InstancedMesh(geometry, material, PARTICLE_COUNT);
  scene.add(mesh);
  return mesh;
}

// ============================================
// MAIN SETUP
// ============================================

let camera, scene, renderer, controls;
let visualization;

async function init() {
  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x111122);

  // Camera
  camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.set(0, 5, 15);

  // Lights
  const ambientLight = new THREE.AmbientLight(0x404040);
  scene.add(ambientLight);

  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(5, 10, 5);
  scene.add(directionalLight);

  // Optional: Ground plane
  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(20, 20),
    new THREE.MeshStandardNodeMaterial({ color: 0x333333 })
  );
  ground.rotation.x = -Math.PI / 2;
  scene.add(ground);

  // Renderer
  renderer = new THREE.WebGPURenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  document.body.appendChild(renderer.domElement);
  await renderer.init();

  // Initialize particles
  await renderer.computeAsync(computeInit);

  // Create visualization
  visualization = createVisualization(scene);

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.target.set(0, 2, 0);

  // Events
  window.addEventListener('resize', onWindowResize);

  // Start
  renderer.setAnimationLoop(animate);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

const clock = new THREE.Clock();

function animate() {
  // Update delta time uniform
  dt.value = Math.min(clock.getDelta(), 0.1);

  // Run compute shaders
  renderer.compute(computeUpdate);
  // renderer.compute(computeInteraction);

  // Update controls
  controls.update();

  // Render
  renderer.render(scene, camera);
}

init().catch(console.error);

// Export for external control
export {
  positions,
  velocities,
  dt,
  computeInit,
  computeUpdate,
  computeInteraction
};
```

## File: `skills/webgpu-threejs-tsl/templates/webgpu-project.js`
```javascript
/**
 * WebGPU Three.js Project Template
 *
 * A complete starter template with:
 * - WebGPU renderer setup
 * - TSL material example
 * - Post-processing ready
 * - Responsive design
 * - Animation loop
 *
 * Usage:
 * 1. Copy this file to your project
 * 2. Install Three.js: npm install three
 * 3. Replace placeholder content with your scene
 */

import * as THREE from 'three/webgpu';
import {
  // Types
  float,
  vec2,
  vec3,
  vec4,
  color,
  uniform,

  // Geometry
  positionLocal,
  positionWorld,
  normalLocal,
  normalWorld,
  uv,

  // Camera
  cameraPosition,

  // Time
  time,
  deltaTime,

  // Math
  mix,
  smoothstep,
  clamp,
  sin,
  cos,

  // Texture
  texture,

  // Functions
  Fn,
  If,
  Loop,

  // Post-processing
  pass
} from 'three/tsl';

import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// ============================================
// CONFIGURATION
// ============================================

const CONFIG = {
  // Renderer
  antialias: true,
  pixelRatio: Math.min(window.devicePixelRatio, 2),

  // Camera
  fov: 60,
  near: 0.1,
  far: 1000,
  position: new THREE.Vector3(0, 2, 5),

  // Scene
  backgroundColor: 0x111111,

  // Controls
  enableDamping: true,
  dampingFactor: 0.05
};

// ============================================
// GLOBALS
// ============================================

let camera, scene, renderer, controls;
let clock;

// Add your uniforms here
const uniforms = {
  // Example: myColor: uniform(new THREE.Color(0xff0000))
};

// ============================================
// INITIALIZATION
// ============================================

async function init() {
  // Clock
  clock = new THREE.Clock();

  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(CONFIG.backgroundColor);

  // Camera
  camera = new THREE.PerspectiveCamera(
    CONFIG.fov,
    window.innerWidth / window.innerHeight,
    CONFIG.near,
    CONFIG.far
  );
  camera.position.copy(CONFIG.position);

  // Renderer
  renderer = new THREE.WebGPURenderer({ antialias: CONFIG.antialias });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(CONFIG.pixelRatio);
  document.body.appendChild(renderer.domElement);

  // Initialize WebGPU
  await renderer.init();

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = CONFIG.enableDamping;
  controls.dampingFactor = CONFIG.dampingFactor;

  // Setup scene content
  setupLights();
  setupScene();

  // Optional: Setup post-processing
  // setupPostProcessing();

  // Events
  window.addEventListener('resize', onWindowResize);

  // Start animation loop
  renderer.setAnimationLoop(animate);
}

// ============================================
// SCENE SETUP
// ============================================

function setupLights() {
  // Ambient light
  const ambientLight = new THREE.AmbientLight(0x404040, 0.5);
  scene.add(ambientLight);

  // Directional light
  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(5, 10, 5);
  directionalLight.castShadow = true;
  scene.add(directionalLight);

  // Add more lights as needed
}

function setupScene() {
  // ========================================
  // ADD YOUR SCENE CONTENT HERE
  // ========================================

  // Example: Create a mesh with TSL material
  const geometry = new THREE.BoxGeometry(1, 1, 1);
  const material = createExampleMaterial();
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  // Example: Add a floor
  const floorGeometry = new THREE.PlaneGeometry(10, 10);
  const floorMaterial = new THREE.MeshStandardNodeMaterial({
    color: 0x333333
  });
  const floor = new THREE.Mesh(floorGeometry, floorMaterial);
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -0.5;
  scene.add(floor);
}

function createExampleMaterial() {
  const material = new THREE.MeshStandardNodeMaterial();

  // ========================================
  // CUSTOMIZE YOUR MATERIAL HERE
  // ========================================

  // Example: Animated color
  material.colorNode = Fn(() => {
    const t = time.mul(0.5).sin().mul(0.5).add(0.5);
    return mix(color(0x0066ff), color(0xff6600), t);
  })();

  // Example: PBR properties
  material.roughnessNode = float(0.5);
  material.metalnessNode = float(0.0);

  // Example: Simple fresnel rim
  material.emissiveNode = Fn(() => {
    const viewDir = cameraPosition.sub(positionWorld).normalize();
    const fresnel = float(1.0).sub(normalWorld.dot(viewDir).saturate()).pow(3.0);
    return color(0x00ffff).mul(fresnel).mul(0.5);
  })();

  return material;
}

// ============================================
// POST-PROCESSING (Optional)
// ============================================

let postProcessing;

function setupPostProcessing() {
  // Uncomment and customize as needed

  // postProcessing = new THREE.PostProcessing(renderer);
  // const scenePass = pass(scene, camera);
  // const sceneColor = scenePass.getTextureNode('output');
  //
  // // Add effects here
  // postProcessing.outputNode = sceneColor;
}

// ============================================
// ANIMATION LOOP
// ============================================

function animate() {
  const delta = clock.getDelta();
  const elapsed = clock.getElapsedTime();

  // ========================================
  // UPDATE YOUR SCENE HERE
  // ========================================

  // Example: Rotate mesh
  const mesh = scene.children.find((child) => child.type === 'Mesh');
  if (mesh) {
    mesh.rotation.y += delta * 0.5;
  }

  // Update controls
  controls.update();

  // Render
  if (postProcessing) {
    postProcessing.render();
  } else {
    renderer.render(scene, camera);
  }
}

// ============================================
// EVENT HANDLERS
// ============================================

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

// ============================================
// START
// ============================================

init().catch(console.error);

// Export for external access if needed
export { scene, camera, renderer, uniforms };
```

