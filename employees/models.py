from mongoengine import Document, EmbeddedDocument, fields


class Project(EmbeddedDocument):
    projectId = fields.StringField(max_length=10, required=True, null=False)
    projectName = fields.StringField(max_length=100, required=True)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()


class Skill(EmbeddedDocument):
    technology = fields.StringField(max_length=100, required=True, null=False)
    experience = fields.StringField(max_length=10, required=True, null=False)
    level = fields.StringField(max_length=10, required=True, null=False)


class Employee(Document):
    employeeId = fields.StringField(max_length=10, required=True, null=False)
    employeeName = fields.StringField(max_length=100, required=True)
    workLocation = fields.StringField(max_length=100, required=True)
    projects = fields.EmbeddedDocumentListField(Project)
    skills = fields.EmbeddedDocumentListField(Skill)