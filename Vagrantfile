# vi: set ft=ruby :

$provision = <<SCRIPT
sudo apt-get update

sudo apt-get install -y python-virtualenv

# Since we're in a VM, move to the shared directory.
# If you're consulting this for setting up webdriver
# outside of a VM, ignore this.
cd /vagrant

virtualenv venv --python=python3
# venv/bin/pip is 1.5.4
venv/bin/pip install --upgrade pip
# venv/bin/pip is pip now 10.0.1, which copes a lot better

venv/bin/pip install -r requirements.txt

SCRIPT

Vagrant.configure("2") do |config|
    # config.vm.box = "debian/jessie64"  # alas, no guest additions in this box
    config.vm.box = "ubuntu/xenial64"
    config.vm.network "forwarded_port", guest: 5000, host: 5000

    config.vm.provider "virtualbox" do |vb|
        vb.name = "Celery Starter"
        vb.memory = 2048
        vb.cpus = 1
    end

    config.vm.provision "file", source: "~/.gitconfig", destination: ".gitconfig"
    config.vm.provision :shell, inline: $provision, privileged: false
end
