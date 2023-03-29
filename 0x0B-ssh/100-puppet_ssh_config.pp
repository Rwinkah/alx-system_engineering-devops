# Puppet manifest to declare the state of an ssh config file
file_line {'Turning off password authentication':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   =>  'PasswordAuthentication no'
}

file_line { 'Declaring an identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school
}
