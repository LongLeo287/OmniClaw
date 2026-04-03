#!/bin/bash
set -e

VERSION=$(cat VERSION | tr -d '[:space:]')

if [ -z "$VERSION" ]; then
    echo "Error: VERSION file is empty"
    exit 1
fi

PLATFORMS="linux/amd64,linux/arm64"

echo "=== Building CQA v${VERSION} (${PLATFORMS}) ==="

# Ensure buildx builder exists
docker buildx inspect cqa-builder >/dev/null 2>&1 || \
    docker buildx create --name cqa-builder --use
docker buildx use cqa-builder

# Build and push app image (multi-platform)
echo "Building buitanviet/chat-quality-agent:${VERSION}..."
docker buildx build \
    --platform "${PLATFORMS}" \
    --build-arg VERSION="${VERSION}" \
    -t "buitanviet/chat-quality-agent:${VERSION}" \
    -t "buitanviet/chat-quality-agent:latest" \
    --push \
    .

# Build and push nginx image (multi-platform)
echo "Building buitanviet/chat-quality-agent-nginx:${VERSION}..."
docker buildx build \
    --platform "${PLATFORMS}" \
    -f docker/Dockerfile.nginx \
    -t "buitanviet/chat-quality-agent-nginx:${VERSION}" \
    -t "buitanviet/chat-quality-agent-nginx:latest" \
    --push \
    .

echo ""
echo "=== Done! Released v${VERSION} (amd64 + arm64) ==="
