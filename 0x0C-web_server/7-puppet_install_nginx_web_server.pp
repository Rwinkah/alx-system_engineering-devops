# server config using puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update -y',
  provider => shell,
}

exec {'Hello World!':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.google.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'start_server':
  command  => 'sudo service nginx restart',
  provider => shell,
}
