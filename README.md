## Домашнее задание №3. Ansible

### Задание

С помощью Ansible проделать следующее.

1. Установить nginx
   

2. Изменить конфигурацию nginx таким образом, чтобы по запросу `GET /service_data` отдавалось содержимое файла `/opt/service_state`


3. Разместить в `/opt/` файл `service_state` состоящий из 2 строк:
```
Seems work
Service uptime is 0 minutes
```
4. Обеспечить запуск nginx
   

5. Добавить в `cron` выполнение раз в минуту команды:
```bash
sed -i "s/is .*$/is $(($(ps -o etimes= -p $(cat /var/run/nginx.pid)) / 60)) minutes/" /opt/service_state
```
6. Написать в ansible проверку на то, что значение uptime в файле `/opt/service_state` начало изменяться.


7. Привести конфигурацию ansible к идемпотентной, до соответствия следующим требованиям:
- повторный запуск ansible с той же конфигурацией не должен сбрасывать значение uptime в файле `/opt/service_state` и не должен рестартовать nginx
- после изменения первой строки service_state, например на "Seems work ok" должно происходить обновление файла `/opt/service_state` и restart сервиса nginx



### Запуск

**1. Комментарии к решению**

`Vagrantfile` с лекции, добавлены только команды для проброса ключей. 

Ключик должен называться стандартно `id_rsa`, либо необходимо внести изменения в `Vagrantfile` и в `group_vars/all`. 

IP адреса виртуалок нужно указать в файле `hosts`.

**2. Запуск**

```
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i ./hosts ./site.yml
```

**P.S.** Во время выполнения playbook таска "File start changing test" не зависает, а ждет около минуты и проверяет, что файлик `service_state` начал изменяться. 

