#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
FCTE / UnB - Qualidade de Software 1 (2026-2)
Grupo 01: Betty Snyder
Script: coletar_ambiente.py (Atendimento à Issue E2-02)
Autor: Dupla B (Eficiência de Desempenho)
===============================================================================
Finalidade:
  Detectar automaticamente as especificações de hardware e software do
  computador do integrante (Sistema Operacional, Processador, Memória RAM,
  Armazenamento e Placa de Vídeo) e gerar a linha formatada em Markdown
  para a tabela oficial de ambiente:
    - docs/avaliacao/protocolos/ambiente.md (Seção 2)
===============================================================================
"""

import sys
import os
import platform
import subprocess

try:
    import psutil
except ImportError:
    psutil = None


def obter_sistema_operacional():
    sistema = platform.system()
    if sistema == "Linux":
        try:
            with open("/etc/os-release", "r") as f:
                for linha in f:
                    if linha.startswith("PRETTY_NAME="):
                        return linha.split("=", 1)[1].strip().strip('"')
        except IOError:
            pass
        return f"Linux ({platform.release()})"
    elif sistema == "Darwin":
        return f"macOS {platform.mac_ver()[0]}"
    elif sistema == "Windows":
        return f"Windows {platform.release()} ({platform.version()})"
    return sistema


def detectar_ambiente_virtual():
    # Heurística para detectar Máquina Virtual (VM) vs Nativo
    sistema = platform.system().lower()
    if "linux" in sistema:
        try:
            saida = subprocess.check_output("systemd-detect-virt", shell=True, stderr=subprocess.DEVNULL).decode().strip()
            if saida and saida != "none":
                return f"VM ({saida})"
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
    return "Nativo"


def obter_processador():
    if platform.system() == "Linux":
        try:
            with open("/proc/cpuinfo", "r") as f:
                for linha in f:
                    if "model name" in linha:
                        return linha.split(":", 1)[1].strip()
        except IOError:
            pass
    elif platform.system() == "Darwin":
        try:
            return subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"]).decode().strip()
        except Exception:
            pass
    elif platform.system() == "Windows":
        return platform.processor()
    return platform.processor() or "Processador Desconhecido"


def obter_memoria_ram():
    if psutil:
        total_gb = round(psutil.virtual_memory().total / (1024 ** 3))
        return f"{total_gb} GB"
    elif platform.system() == "Linux":
        try:
            with open("/proc/meminfo", "r") as f:
                for linha in f:
                    if "MemTotal" in linha:
                        kb = int(linha.split()[1])
                        return f"{round(kb / (1024 * 1024))} GB"
        except IOError:
            pass
    return "N/D"


def obter_armazenamento():
    if platform.system() == "Linux":
        try:
            # Verifica se o disco raiz é rotacional (HDD=1, SSD=0)
            with open("/sys/block/sda/queue/rotational", "r") as f:
                return "HDD" if f.read().strip() == "1" else "SSD"
        except IOError:
            try:
                with open("/sys/block/nvme0n1/queue/rotational", "r") as f:
                    return "SSD NVMe"
            except IOError:
                pass
    return "SSD"


def obter_gpu():
    if platform.system() == "Linux":
        try:
            lspci = subprocess.check_output("lspci", shell=True, stderr=subprocess.DEVNULL).decode()
            for l in lspci.splitlines():
                if "VGA" in l or "3D" in l:
                    gpu = l.split(":", 2)[-1].strip()
                    if "Intel" in gpu:
                        return "Intel Graphics (Integrada)"
                    elif "NVIDIA" in gpu:
                        return "NVIDIA Dedicada"
                    elif "AMD" in gpu:
                        return "AMD Radeon"
                    return gpu
        except Exception:
            pass
    return "Integrada"


def main():
    print("=" * 72)
    print("💻 BETTY SNYDER - COLETOR DE ESPECIFICAÇÕES DO AMBIENTE (ISSUE E2-02)")
    print("=" * 72)

    so = obter_sistema_operacional()
    tipo_env = detectar_ambiente_virtual()
    cpu = obter_processador()
    ram = obter_memoria_ram()
    disco = obter_armazenamento()
    gpu = obter_gpu()

    print(f"• Sistema Operacional: {so}")
    print(f"• Tipo de Ambiente:    {tipo_env}")
    print(f"• Processador:         {cpu}")
    print(f"• Memória RAM:         {ram}")
    print(f"• Armazenamento:       {disco}")
    print(f"• Placa de Vídeo:      {gpu}")
    print("-" * 72)
    print("📋 Linha formatada para a Tabela de 'docs/avaliacao/protocolos/ambiente.md':\n")
    print(f"| [Seu Nome](https://github.com/seu-user) | {so} | {tipo_env} | {cpu} | {ram} | {disco} | {gpu} |")
    print("=" * 72)


if __name__ == "__main__":
    main()
