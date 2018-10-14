## Configuration Manager
The most of configuration managers using lot of system resource. With this program you can manage your system's files, run custom command and store many outputs to a central based storage. This program using Jinja2 templates and you'll use variables in template files.

###Catalog
Catalog is a YAML based file. Catalog name is its file name.

Every Catalog must start with:
`---`

###Catalog Task
You can declare unlimited tasks in Catalog. In task you can create one resource definition only!

```
  ...
  tasks:
    - name: TASK_NAME
        ...
        ...
        ...
      register: VARIABLE_NAME
```

###Resource definition
#####ReadEnv resource:
You can read system environment variables and store variable value. If ENV not exists in the system, you can set 'default' attribute.
```
    readenv:
      name: ENV_NAME
      [default: DEFAULT_VALUE]
```
default attribute is optional!

#####File resource
|        | type              | require | default | conditional         |
|--------|-------------------|---------|---------|---------------------|
| path   | Unix Path         | True    | None    |                     |
| state  | [present, absent] | False   | present |                     |
| owner  | String            | False   | root    |                     |
| group  | String            | False   | root    |                     |
| mode   | String            | False   | 0600    |                     |
| source | Unix Path         | False   | None    | if state == present |

Example:
```
    file:
      path:  /var/www/html/index.html
      state: present
      owner: www-data
      group: www-data
      mode:  0755
      source: /root/index.html.j2
```
###Full example
```
&#45; &#45; &#45;
tasks:
  - name: 'Read PHP_FPM_USING_MODE'
    readenv:
      name: USER
      default: 'test'
    register: user
  - name: 'Test task'
    file:
      path:  /var/www/html/index.html
      state: present
      owner: www-data
      group: www-data
      mode:  0755
      source: /root/index.html.j2
```

