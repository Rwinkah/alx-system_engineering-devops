# Puppet Manifest to create a file named school in tmp
# File permissions are 0744
# File owner and group are both www-data

file {'/tmp/school':
    ensure  => present,
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
