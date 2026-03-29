FROM ubuntu:22.04

RUN apt update && apt install -y \
    python3 \
    g++ \
    openjdk-11-jdk

WORKDIR /app

COPY sandbox /app/

RUN useradd -m sandboxuser

# ✅ GIVE PERMISSION
RUN chown -R sandboxuser:sandboxuser /app

USER sandboxuser

CMD ["bash"]
