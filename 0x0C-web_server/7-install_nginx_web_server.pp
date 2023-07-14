# puppet script to setup server
package { 'nginx':
  ensure => 'installed',
}

exec { 'repo_update':
  command => 'sudo apt-get update -y',
  provider => shell,
}

exec { 'index_page':
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'start_server':
  command => 'sudo service nginx restart',
  provider => shell,
}

