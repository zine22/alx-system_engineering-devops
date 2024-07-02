# Puppet manifest containing commands to automatically configure an Ubuntu machine and install Nginx

package { 'nginx':
  ensure => installed,
}

file_line { 'server_config':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/,
  }

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}