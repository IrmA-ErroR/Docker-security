# Практика: Безопасность контейнеров
  

Необходимо развернуть окружение с веб-сайтом с использованием базы данных, настроить постоянное хранение и создать сетевое окружение. Проверить получившийся контейнер и образ на безопасность. В отчете привести скриншоты и описать последовательность действий. Разобрать вывод сканеров безопасности и предложить меры по их исправлению.

## Install docker
Установка скриптом из официальной документации:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
# Add user to group
sudo usermod -aG docker $(whoami)
```
