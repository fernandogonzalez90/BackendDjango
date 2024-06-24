provider "aws" {
  region = "sa-east-1" # Brazil
}

resource "aws_instance" "django_server" {
  ami           = "ami-0c0746ac7168488ae" # Debian
  instance_type = "t3.micro"
  key_name      = aws_key_pair.django-key.key_name

  vpc_security_group_ids = [aws_security_group.django_sg.id]

  tags = {
    Name = "DjangoServer"
  }

  provisioner "local-exec" {
    command = <<-EOT
      sleep 60  # Espera 60 segundos antes de ejecutar los comandos
      echo "[django]
      ${self.public_ip} ansible_user=admin ansible_ssh_private_key_file=~/.ssh/id_rsa" > ../Ansible/hosts.ini
      ansible-playbook -i ../Ansible/hosts.ini ../Ansible/django_setup.yaml --ssh-common-args='-o StrictHostKeyChecking=no' --extra-vars "server_ip=${self.public_ip}"
    EOT
  }
}

resource "aws_security_group" "django_sg" {
  name_prefix = "django-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "django-key" {
  key_name   = "django_key"
  public_key = file("clave.pub")
}

output "django_url" {
  value = "http://${aws_instance.django_server.public_ip}:8080"
}
