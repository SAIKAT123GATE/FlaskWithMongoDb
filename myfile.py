# coding: utf-8
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AccessLevel(Base):
    __tablename__ = 'AccessLevel'

    AccessLevelId = Column(INTEGER(11), primary_key=True)
    AccessLevelName = Column(String(45), nullable=False)


class Designation(Base):
    __tablename__ = 'Designation'

    DesignationId = Column(INTEGER(11), primary_key=True)
    DesignationName = Column(String(45), nullable=False)
    EntityTypeId = Column(INTEGER(11), nullable=False)


class EntityType(Base):
    __tablename__ = 'EntityType'

    EntityTypeId = Column(INTEGER(11), primary_key=True)
    EntityTypeName = Column(String(45))


class PermissionGroup(Base):
    __tablename__ = 'PermissionGroup'

    PermissionGroupId = Column(INTEGER(11), primary_key=True)
    Name = Column(String(45))
    Description = Column(String(45))


class Role(Base):
    __tablename__ = 'Role'

    RoleId = Column(INTEGER(11), primary_key=True)
    RoleName = Column(String(45))
    Description = Column(String(45))


class User(Base):
    __tablename__ = 'User'

    UserId = Column(INTEGER(11), primary_key=True)
    FirstName = Column(String(200), nullable=False)
    LastName = Column(String(200))
    Email = Column(String(100), nullable=False)


class Entity(Base):
    __tablename__ = 'Entity'

    EntityId = Column(INTEGER(11), primary_key=True)
    EntityName = Column(String(45), nullable=False)
    EntityTypeId = Column(ForeignKey('EntityType.EntityTypeId'), nullable=False, index=True)

    EntityType = relationship('EntityType')


class Permission(Base):
    __tablename__ = 'Permission'

    PermissionId = Column(INTEGER(11), primary_key=True)
    Name = Column(String(45))
    Description = Column(String(45))
    PermissionGroupId = Column(ForeignKey('PermissionGroup.PermissionGroupId'), nullable=False, index=True)

    PermissionGroup = relationship('PermissionGroup')


class RolePermissionGroupMapping(Base):
    __tablename__ = 'RolePermissionGroupMapping'

    RolePermissionGroupMappingId = Column(INTEGER(11), primary_key=True)
    RoleId = Column(ForeignKey('Role.RoleId'), nullable=False, index=True)
    PermissionGroupId = Column(ForeignKey('PermissionGroup.PermissionGroupId'), nullable=False, index=True)

    PermissionGroup = relationship('PermissionGroup')
    Role = relationship('Role')


class UserRoleMapping(Base):
    __tablename__ = 'UserRoleMapping'

    UserRoleMappingId = Column(INTEGER(11), primary_key=True)
    UserId = Column(ForeignKey('User.UserId'), nullable=False, index=True)
    RoleId = Column(ForeignKey('Role.RoleId'), nullable=False, index=True)

    Role = relationship('Role')
    User = relationship('User')


class EntityMapping(Base):
    __tablename__ = 'EntityMapping'

    EntityMappingId = Column(INTEGER(11), primary_key=True)
    EntityId = Column(ForeignKey('Entity.EntityId'), nullable=False, index=True)
    ParentEntityId = Column(ForeignKey('Entity.EntityId'), nullable=False, index=True)

    Entity = relationship('Entity', primaryjoin='EntityMapping.EntityId == Entity.EntityId')
    Entity1 = relationship('Entity', primaryjoin='EntityMapping.ParentEntityId == Entity.EntityId')


class RolePermissionMapping(Base):
    __tablename__ = 'RolePermissionMapping'

    RolePermissionMappingId = Column(INTEGER(11), primary_key=True)
    RoleId = Column(ForeignKey('Role.RoleId'), nullable=False, index=True)
    PermissionId = Column(ForeignKey('Permission.PermissionId'), nullable=False, index=True)

    Permission = relationship('Permission')
    Role = relationship('Role')


class UserEntityMapping(Base):
    __tablename__ = 'UserEntityMapping'

    UserEntityMappingId = Column(INTEGER(11), primary_key=True)
    UserId = Column(ForeignKey('User.UserId'), nullable=False, index=True)
    EntityId = Column(ForeignKey('Entity.EntityId'), nullable=False, index=True)
    DesignationId = Column(ForeignKey('Designation.DesignationId'), nullable=False, index=True)
    AccessLevelId = Column(ForeignKey('AccessLevel.AccessLevelId'), nullable=False, index=True)

    AccessLevel = relationship('AccessLevel')
    Designation = relationship('Designation')
    Entity = relationship('Entity')
    User = relationship('User')
