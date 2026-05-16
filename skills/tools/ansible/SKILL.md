---
name: ansible
version: 1.0.0
description: "Provides comprehensive guidance for Ansible automation including playbooks, roles, inventory, and module usage. Use when the user asks about Ansible, needs to automate IT tasks, create Ansible playbooks, or manage infrastructure with Ansible."
author: Fullstack Skills Community
category: tools
tags: [ansible]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

- name: Deploy web application
  hosts: webservers
  become: true
  vars:
    app_port: 8080
  tasks:
    - name: Install nginx
      ansible.builtin.package:
        name: nginx
        state: present

    - name: Deploy config from template
      ansible.builtin.template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: restart nginx

  handlers:
    - name: restart nginx
      ansible.builtin.service:
        name: nginx
        state: restarted
```

```bash
# Run the playbook
ansible-playbook -i inventory/production site.yml

# Ad-hoc ping all hosts
ansible -m ping all
```

### Key Commands

| Command | Purpose |
|---------|---------|
| `ansible-playbook playbook.yml` | Run a playbook |
| `ansible -m ping all` | Test connectivity |
| `ansible-vault encrypt vars/secrets.yml` | Encrypt sensitive data |
| `ansible-galaxy init myrole` | Scaffold a new role |

## Best Practices

- Organize with roles and `group_vars/host_vars` hierarchy; avoid monolithic playbooks
- Encrypt sensitive data with `ansible-vault`; use idempotent tasks with `state` and conditionals
- Define explicit failure handling (`ignore_errors`, `block/rescue`); use tags for selective runs
- Control node requires Python; target hosts need SSH access; optionally use AWX/Tower for scheduling

## Troubleshooting

- **Connection refused**: Verify SSH keys and `ansible_user` in inventory
- **Module not found**: Check Ansible version and use FQCN (e.g., `ansible.builtin.copy`)
- **Idempotency failures**: Ensure tasks use `state` parameter and avoid shell commands where modules exist

## Keywords

ansible, playbook, role, inventory, automation, configuration management, ansible-vault, infrastructure
