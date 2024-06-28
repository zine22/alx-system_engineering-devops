# Using Puppet, install flask from pip3

exec {'install_flask':
  command => '/usr/bin/pip install flask==2.1.0',
  creates => '/usr/local/lib/python3.6/dist-packages/flask'
}

# package { 'puppet-lint':
#   ensure   => '2.1.1',
#   provider => 'gem'
# }