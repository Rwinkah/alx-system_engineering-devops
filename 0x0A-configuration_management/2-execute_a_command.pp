# Manifest to kill a running task
exec { 'killing a process using pkill':
    command  => 'pkill -9 killmenow',
    path     => '/usr/bin:/bin',
    onlyif   => 'pgrep killmenow',
    provider => shell,
}
