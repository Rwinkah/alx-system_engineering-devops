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

exec {'redirect':
	command => sed -i 'i 47i \\tlocation /redirect_me {\n\t\treturn 301 http://www.google.com;\n\t}'

