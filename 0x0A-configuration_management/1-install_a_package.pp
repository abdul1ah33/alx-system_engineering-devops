# 1-install_a_package.pp
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep "Version: 2.1.0"',
  path    => ['/bin', '/usr/bin'],
  require => Package['python3-pip'],
}

package { 'python3-pip':
  ensure => installed,
}

