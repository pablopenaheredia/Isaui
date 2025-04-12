use base_peluqueria;
create table if not exists servicio(
id_servicio int not null auto_increment,
descripcion varchar(500) not null,
tiempo_estimado time not null,
nombre varchar(500) not null,
primary key(id_servicio)
);
create table if not exists producto(
id_producto int not null auto_increment,
nombre varchar(500) not null,
marcar varchar(500) not null,
cantidad float not null,
precio  float not null,
primary key(id_producto)
);
create table if not exists turno(
id_turno int not null auto_increment,
fecha date not null,
hora time not null,
id_servicio int,
primary key (id_turno),
foreign key(id_servicio)references servicio(id_servicio)
);
create table if  not exists tipo_p(
id_tipo_p int not null auto_increment,
tipo varchar(200) not null,
primary key(id_tipo_p)
);
create table if not exists persona(
id_persona int not null auto_increment,
nombre varchar(200) not null,
apellido varchar(200)not null,
dni varchar(200) not null,
contacto varchar(200) not null,
tipo varchar(200) not null,
activo varchar(200) not null,
id_tipo_p int,
id_turno int,
correo varchar(200) not null,
primary key(id_persona),
foreign key (id_tipo_p)references tipo_p(id_tipo_p),
foreign key (id_turno) references turno(id_turno)
);



ALTER TABLE `base_peluqueria`.`turno` 
ADD COLUMN `cliente` VARCHAR(150) NOT NULL AFTER `id_servicio`;
