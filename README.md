# 1. Neko-Chan2

猫猫ちゃん二代目源代码。[初代目](https://github.com/qzlzdy/Neko-Chan.git)

- [1. Neko-Chan2](#1-neko-chan2)
- [2. Prerequistes](#2-prerequistes)
  - [2.1. Install NoneBot2](#21-install-nonebot2)
    - [2.1.1. Install Driver](#211-install-driver)
    - [2.1.2. Install adapter install mirai](#212-install-adapter-install-mirai)
    - [2.1.3. Fix issues](#213-fix-issues)
    - [2.1.4. Install plugin](#214-install-plugin)
  - [2.2. Install Mirai2](#22-install-mirai2)
    - [2.2.1. Install plugin](#221-install-plugin)
    - [2.2.2. Configure plugin](#222-configure-plugin)
    - [2.2.3. Configure `.env`](#223-configure-env)
- [3. Start Bot](#3-start-bot)

# 2. Prerequistes

## 2.1. Install NoneBot2

```bash
python -m venv Nekochan
cd Nekochan
source bin/activate
pip install nb-cli
```

### 2.1.1. Install Driver

```bash
nb driver install nonebot2[fastapi]
nb driver install nonebot2[websockets]
```

### 2.1.2. Install adapter install mirai

```bash
nb adapter install nonebot_adapter_mirai2
```

### 2.1.3. Fix issues

```bash
pip install --force-reinstall 'pydantic~=1.10'
```

### 2.1.4. Install plugin

```bash
nb plugin install nonebot-plugin-apscheduler
```

## 2.2. Install Mirai2

下载安装包[iTXTech/mcl-installer](https://github.com/iTXTech/mcl-installer/releases)并运行

### 2.2.1. Install plugin

```bash
./mcl --update-package net.mamoe:mirai-api-http --type plugin --channel stable-v2
```

### 2.2.2. Configure plugin

运行一次，配置QQ号，退出

```bash
./mcl -u
```

编辑产生的配置文件

```bash
cat << EOF > ${MIRAI2_ROOT}/config/net.mamoe.mirai-api-http/setting.yml
adapters:
  - ws
debug: false
enableVerify: true
verifyKey: WRITE_YOUR_KEY_HERE
singleMode: false
cacheSize: 2048
adapterSettings:
  ws:
    host: 127.0.0.1
    port: 5700
EOF
```

### 2.2.3. Configure `.env`

```bash
cat << EOF > .env
ENVIRONMENT=prod
VERIFY_KEY=WRITE_YOUR_KEY_HERE
driver=~fastapi+~websockets

MIRAI_HOST=127.0.0.1
MIRAI_PORT=5700
MIRAI_QQ=["123456789"]
SUPERUSERS=[]
EOF
```

# 3. Start Bot

```bash
./mcl -u # Start Mirai2 first
nb run   # Start Nonebot2
```
