# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'etc'

def form_ips(is_home = "false", num = 0)
    @is_home = is_home.to_s.downcase == "true"
    @header = "10.211."
    if @is_home
        return "%s100.%d" % [@header, 100 + num]
    else
        @suffix = Etc.getlogin[-3..-1].to_i * 3
        return "%s%d.%d" % [@header, @suffix / 256, @suffix % 256 - num]
    end
end

@ip1 = form_ips ENV['IS_HOME'], 2
@ip2 = form_ips ENV['IS_HOME'], 1
@ip3 = form_ips ENV['IS_HOME']
puts "This script will start these VMs:"
puts "%s-node1 with IP %s" % [Etc.getlogin, @ip1]
puts "%s-node2 with IP %s" % [Etc.getlogin, @ip2]
puts "%s-node3 with IP %s" % [Etc.getlogin, @ip3]

$update_ubuntu = <<SCRIPT
apt update
apt install python-dev python3-dev -y
SCRIPT

$update_centos = <<SCRIPT
sudo yum -y install python-devel python3-devel
SCRIPT

Vagrant.configure("2") do |config|
  config.hostmanager.enabled = false
  config.hostmanager.manage_guest = true
  config.hostmanager.include_offline = true
  config.hostmanager.ignore_private_ip = false
  config.ssh.forward_agent = true
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/me.pub"
  config.vm.provision "shell", inline: <<-SHELL
    cat /home/vagrant/.ssh/me.pub >> /home/vagrant/.ssh/authorized_keys
  SHELL

  config.vm.define :node1 do |node1|
    node1.vm.box = "ubuntu/bionic64"
    node1.vm.provider "virtualbox" do |vb|
      vb.cpus = "1"
      vb.memory = "1024"
    end
    node1.vm.network :private_network, ip: @ip1
    node1.vm.hostname = Etc.getlogin + "-node1"
    node1.vm.provision :hostmanager
    node1.vm.provision :shell, :inline => $update_ubuntu
    node1.vm.provision :shell, inline: <<-SHELL
      sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
      sudo service ssh restart
    SHELL
  end

  config.vm.define :node2 do |node2|
    node2.vm.box = "ubuntu/trusty64"
    node2.vm.provider "virtualbox" do |vb|
      vb.cpus = "1"
      vb.memory = "1024"
    end
    node2.vm.network :private_network, ip: @ip2
    node2.vm.hostname = Etc.getlogin + "-node2"
    node2.vm.provision :hostmanager
    node2.vm.provision :shell, :inline => $update_ubuntu
    node2.vm.provision :shell, inline: <<-SHELL
      sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
      sudo service ssh restart
    SHELL
  end

  config.vm.define :node3 do |node3|
    node3.vm.box = "centos/7"
    node3.vm.provider "virtualbox" do |vb|
      vb.cpus = "1"
      vb.memory = "1024"
    end
    node3.vm.network :private_network, ip: @ip3
    node3.vm.hostname = Etc.getlogin + "-node3"
    node3.vm.provision :hostmanager
    node3.vm.provision :shell, :inline => $update_centos
    node3.vm.provision :shell, inline: <<-SHELL
      sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
      sudo systemctl restart sshd
    SHELL
  end
end

