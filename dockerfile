
# FROM debian:bookworm-slim
# FROM debian:11.10-slim
# FROM debian:10.1
# FROM ubuntu:13.10
FROM python:3.6.15-slim


LABEL \
  org.opencontainers.image.title="Test" \
  org.opencontainers.image.description="a docker container" \
  org.opencontainers.image.documentation="https://nofusscomputing.com" \
  org.opencontainers.image.vendor="No Fuss Computing" \
  io.artifacthub.package.license="MIT"

