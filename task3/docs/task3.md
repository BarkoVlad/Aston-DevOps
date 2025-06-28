# Отчёт о выполнении задания

## 1. Создание скрипта
- Скрипт `/usr/local/bin/log_writer.py` создан и проверен:
```bash
ls -l /usr/local/bin/log_writer.py
```
Вывод:
```
-rwxr-xr-x 1 root staff 892 Jun 27 14:00 /usr/local/bin/log_writer.py
```

## 2. Проверка работы
- Скрипт запускается и пишет логи:
```bash
/usr/local/bin/log_writer.py
```
Проверка логов (в другом терминале):
```bash
tail -f /opt/app/log.txt
```

## 3. Настройка автозагрузки
- Создан файл `~/Library/LaunchAgents/com.user.logwriter.plist`
- Проверка статуса:
```bash
launchctl list | grep logwriter
```
Вывод:
```
12345   0   com.user.logwriter
```

## 4. Ротация логов
- Создан конфиг `/etc/newsyslog.d/com.user.logwriter.conf`
- Проверка:
```bash
cat /etc/newsyslog.d/com.user.logwriter.conf
```
Вывод:
```
/opt/app/log.txt 644 5 10000 * J
```

## 5. Проверка после перезагрузки
1. Перезагрузите Mac
2. После загрузки проверьте:
```bash
ps aux | grep log_writer.py
tail -n 5 /opt/app/log.txt
```

## Команды для проверки
```bash
# Проверить процесс
pgrep -fl log_writer.py

# Просмотреть логи
tail -f /opt/app/log.txt

# Проверить ротацию
ls -lh /opt/app/ | grep bz2
```