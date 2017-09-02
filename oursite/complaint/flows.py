from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import complaint

@frontend.register
class complaint(Flow):
	process_class = complaint

	start = (
		flow.Start(
			CreateProcessView,
			fields = ["title"]
		).Permission(
			auto_create = True
		).Next(this.departments)
	)

	departments = (
		flow.View(
			UpdateProcessView,
			fields=["departments"]
		).Permission(
			auto_create = True
		).Next(this.check_approve)
	)

	check_approve = (
		flow.If(lambda activation: activation.process.approved)
		.Then(this.send)
		.Else(this.end)
	)

	send = (
		flow.Handler(
			this.send_complaint_request
		).Next(this.end)
	)

	end = flow.End()

	def send_complaint_request(self, activation):
		print activation.process.text