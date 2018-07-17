Role Name
=========

Standard setup for fresh-built Ubuntu servers

Requirements
------------

None

Role Variables
--------------

Reboot server after setup tasks complete:

    setup_reboot: no

Server timezone and locale

    setup_timezone: America/Los_Angeles
    setup_locale: en_US.UTF-8

Ssh authorized hosts
    setup_authorized_host_keys: []

Ssh host key (instead of sshkeygen). Expects dict with type, public,
private attributes. Typically created with
`ssh-keygen -t rsa -C demo -N '' -b 3072 -f key`

    setup_ssh_host_key:
      
Dependencies
------------


Example Playbook
----------------

    - hosts: servers
      - import_role:
          name: setup
        vars:
          setup_reboot: yes
          setup_authorized_host_keys:
            - 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyFeOZncDip2ZoHu1f8Ap/6xW/SXUrX2sLDKSb0BZLtnVcjFMC6PM+qzumaH2Yup1ztfWcaJGz9o5bl0lzxE/ITOq3+oZ7aSTCn5/PIr41LH0W1gjMCSiS1SU5/UDccOJw3O/gFvUrdH+DiIiioyMrRKso7fLlGzZOOH4vJONzK/0Djpb5ls8ebwdPElNxPYQuPjSY7Ga0YGLk790jK0ejnaJEHt469dJu7lJt7Dhvp1hVlMC75VQ6Pz9svxN+iNEPIy0+YsBQNiwZVs+m3+Cq54KpirvcF8AjWrvrhzZLb2OcUkRibRkrrrCjbcV8kFx2cCo6V4FvRLwJ0CuOKJ8v'
          setup_ssh_host_key:
            type: rsa
            public: 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClVeeSFfP5pBDJHj1BkPeSI64gf6rG4pHibJXH7MMvq34mwjoJN0zAq2+w0ZOJjOpI4fOE26OGIIFV7g9HoBGLbO1azjhDxIxlRhE9+FyV/q83tnUNR/tzbrDpZ5Ckxcm/s6WXNj7EOavHol1smn9xXJlE5+9EEsaWxRHOL7vFXVcpfZYDuzmAJbrB+Ltr6rrW/atjz+lzu7ayL7hT8mVuImv7whsGn2ixob5gsjV7STw2oDGgf722gxEYoujr61tokagtfQY1I/ikGbX9yqlEFCjRfIW7jCDJcWHbQbH2H7RP1XK2UyYK+BjOaa9m/SwhJFS5nxD+WLvyxbmSpuWd demo'
            private: |
              -----BEGIN RSA PRIVATE KEY-----
              MIIEogIBAAKCAQEApVXnkhXz+aQQyR49QZD3kiOuIH+qxuKR4myVx+zDL6t+JsI6
              CTdMwKtvsNGTiYzqSOHzhNujhiCBVe4PR6ARi2ztWs44Q8SMZUYRPfhclf6vN7Z1
              DUf7c26w6WeQpMXJv7OllzY+xDmrx6JdbJp/cVyZROfvRBLGlsURzi+7xV1XKX2W
              A7s5gCW6wfi7a+q61v2rY8/pc7u2si+4U/JlbiJr+8IbBp9osaG+YLI1e0k8NqAx
              oH+9toMRGKLo6+tbaJGoLX0GNSP4pBm1/cqpRBQo0XyFu4wgyXFh20Gx9h+0T9Vy
              tlMmCvgYzmmvZv0sISRUuZ8Q/li78sW5kqblnQIDAQABAoIBABpUjPV544ndNAMj
              erPnZ1XxsrhgPI1B5eO+UTgun4MG96cqhV2UXffNFZN+PNXKCEGlIkgFRoyEvrQ1
              nl9UwZaHuWEduF4qfgVe3D4XQH9uuO7RcuCzlvryJOB26tUi3pdV/8gODn7nhFDd
              ra0vCZ6/FXWgzjz0FIZMSiKg/XFXw4xBODJCXSjjwmjfi5W1l9Qs6awefGcUp3Cj
              A0GD3uP/M25hAk3gF1GlrC/+mKvfEDLQIwoFDDToc0qfZoN8KnQsPm5fHbKqY8z6
              FqqIfbsro+8BGTOLo/vUfxJtBtoUUnfCOug8HMqYh/TbqPf81jGYy51x06mSJMyE
              a9tsxu0CgYEA0+PMS/9pbMOMuzgMFxPYQM3tiQ5LOT+GJOOu4aMunddPL6jwP+wS
              e3yD59RounbpsjE7P4VIIZ0cXssVlQ3s5OKn9iuR06Ojn0SoUKAhpd4JJFHEA1KO
              fnmp3a+HoA1GiOXBf6nAYv5Uh58SMNZ0Prrzuf8jauEDIUlBTtvyDA8CgYEAx8EZ
              ZmJYux6KWPow0aQnb18QoN+0s5l1vzN5dVNPPJEoKoB69eQpddXmCmiamm0XGxui
              Esxn/4mNWRFeG42sGVtjdnAowuv1e+ZAkbjTzvD2EWjPiUlnBLT4ehEvW0uLkt87
              TPt6CXPFkvdHp0o3r42bWHjcBGpbgaCVZ9kBd5MCgYAn50B0F3eNKg54u4dbWTti
              iOVw6CY2c8YZcF9g0tBWnVOmUBRelWCtrLdSk2fdpcNA8ZCM19bLrcDIAUrhNSwl
              tqGW9IGT779CoTVpaZ6sk/H4ywU08vkuzE63FvVdqOJdqZcVKay3d9oHaGeOlvRx
              U9fOcUQEPrfOLvODnFwq9QKBgEh9W+Fa2UZ2i9BEYwkBIEp7XkZzSFlQ3HkZjf80
              z3F0X/Ykj/rB5QXdLNEkKs7VvefZfFSEF02VtlTXR6aKICVHk+28QB6UkI54/X+k
              akEUEsg4l/ADUj5UCkQKDnx8Cteu6Q9Dx4K8n7t4v2kHNvQfWHufyIBVtIVzKCT6
              jFy/AoGAL8SN9ibTjE8YT8INo1bOc066O7FZplI2nF5ZKCX35EsmSUL+1B1iE8vT
              rPeYovN7XBh7xWc835d77UV55taBnmKcBTx3Gb0uEJ350CuZwAGSF+U07xSmKTIY
              QBjYAwIRoOL6wTwPTchEAMBUgjA9rTtQgK2FsNr8DzBDDW9wE7M=
              -----END RSA PRIVATE KEY-----
            