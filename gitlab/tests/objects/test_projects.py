import unittest
import gitlab
import os
import pickle
import tempfile
import json
import unittest
import requests
from gitlab import *  # noqa
from gitlab.v4.objects import *  # noqa
from httmock import HTTMock, urlmatch, response, with_httmock  # noqa

from .mocks import *  # noqa


@urlmatch(
    scheme="http", netloc="localhost", path="/api/v4/projects/1/export", method="get",
)
def resp_export_status(url, request):
    """Mock for Project Export GET response."""
    content = """{
      "id": 1,
      "description": "Itaque perspiciatis minima aspernatur",
      "name": "Gitlab Test",
      "name_with_namespace": "Gitlab Org / Gitlab Test",
      "path": "gitlab-test",
      "path_with_namespace": "gitlab-org/gitlab-test",
      "created_at": "2017-08-29T04:36:44.383Z",
      "export_status": "finished",
      "_links": {
        "api_url": "https://gitlab.test/api/v4/projects/1/export/download",
        "web_url": "https://gitlab.test/gitlab-test/download_export"
      }
    }
    """
    content = content.encode("utf-8")
    return response(200, content, headers, None, 25, request)


@urlmatch(
    scheme="http", netloc="localhost", path="/api/v4/projects/import", method="post",
)
def resp_import_project(url, request):
    """Mock for Project Import POST response."""
    content = """{
      "id": 1,
      "description": null,
      "name": "api-project",
      "name_with_namespace": "Administrator / api-project",
      "path": "api-project",
      "path_with_namespace": "root/api-project",
      "created_at": "2018-02-13T09:05:58.023Z",
      "import_status": "scheduled"
    }"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 25, request)


@urlmatch(
    scheme="http", netloc="localhost", path="/api/v4/projects/1/import", method="get",
)
def resp_import_status(url, request):
    """Mock for Project Import GET response."""
    content = """{
      "id": 1,
      "description": "Itaque perspiciatis minima aspernatur corporis consequatur.",
      "name": "Gitlab Test",
      "name_with_namespace": "Gitlab Org / Gitlab Test",
      "path": "gitlab-test",
      "path_with_namespace": "gitlab-org/gitlab-test",
      "created_at": "2017-08-29T04:36:44.383Z",
      "import_status": "finished"
    }"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 25, request)


@urlmatch(
    scheme="http", netloc="localhost", path="/api/v4/import/github", method="post",
)
def resp_import_github(url, request):
    """Mock for GitHub Project Import POST response."""
    content = """{
    "id": 27,
    "name": "my-repo",
    "full_path": "/root/my-repo",
    "full_name": "Administrator / my-repo"
    }"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 25, request)


@urlmatch(
    scheme="http",
    netloc="localhost",
    path="/api/v4/projects/1/remote_mirrors",
    method="get",
)
def resp_get_remote_mirrors(url, request):
    """Mock for Project Remote Mirrors GET response."""
    content = """[
      {
        "enabled": true,
        "id": 101486,
        "last_error": null,
        "last_successful_update_at": "2020-01-06T17:32:02.823Z",
        "last_update_at": "2020-01-06T17:32:02.823Z",
        "last_update_started_at": "2020-01-06T17:31:55.864Z",
        "only_protected_branches": true,
        "update_status": "finished",
        "url": "https://*****:*****@gitlab.com/gitlab-org/security/gitlab.git"
      }
    ]"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 5, request)


@urlmatch(
    scheme="http",
    netloc="localhost",
    path="/api/v4/projects/1/remote_mirrors",
    method="post",
)
def resp_create_remote_mirror(url, request):
    """Mock for Project Remote Mirrors POST response."""
    content = """{
        "enabled": false,
        "id": 101486,
        "last_error": null,
        "last_successful_update_at": null,
        "last_update_at": null,
        "last_update_started_at": null,
        "only_protected_branches": false,
        "update_status": "none",
        "url": "https://*****:*****@example.com/gitlab/example.git"
    }"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 5, request)


@urlmatch(
    scheme="http",
    netloc="localhost",
    path="/api/v4/projects/1/remote_mirrors/1",
    method="put",
)
def resp_update_remote_mirror(url, request):
    """Mock for Project Remote Mirrors PUT response."""
    content = """{
        "enabled": false,
        "id": 101486,
        "last_error": null,
        "last_successful_update_at": "2020-01-06T17:32:02.823Z",
        "last_update_at": "2020-01-06T17:32:02.823Z",
        "last_update_started_at": "2020-01-06T17:31:55.864Z",
        "only_protected_branches": true,
        "update_status": "finished",
        "url": "https://*****:*****@gitlab.com/gitlab-org/security/gitlab.git"
    }"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 5, request)


@urlmatch(
    scheme="http",
    netloc="localhost",
    path="/api/v4/projects/1/services/pipelines-email",
    method="put",
)
def resp_update_service(url, request):
    """Mock for Service update PUT response."""
    content = """{
        "id": 100152,
        "title": "Pipelines emails",
        "slug": "pipelines-email",
        "created_at": "2019-01-14T08:46:43.637+01:00",
        "updated_at": "2019-07-01T14:10:36.156+02:00",
        "active": true,
        "commit_events": true,
        "push_events": true,
        "issues_events": true,
        "confidential_issues_events": true,
        "merge_requests_events": true,
        "tag_push_events": true,
        "note_events": true,
        "confidential_note_events": true,
        "pipeline_events": true,
        "wiki_page_events": true,
        "job_events": true,
        "comment_on_event_enabled": true,
        "project_id": 1
    }"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 5, request)


@urlmatch(
    scheme="http",
    netloc="localhost",
    path="/api/v4/projects/1/services/pipelines-email",
    method="get",
)
def resp_get_service(url, request):
    """Mock for Service GET response."""
    content = """{
        "id": 100152,
        "title": "Pipelines emails",
        "slug": "pipelines-email",
        "created_at": "2019-01-14T08:46:43.637+01:00",
        "updated_at": "2019-07-01T14:10:36.156+02:00",
        "active": true,
        "commit_events": true,
        "push_events": true,
        "issues_events": true,
        "confidential_issues_events": true,
        "merge_requests_events": true,
        "tag_push_events": true,
        "note_events": true,
        "confidential_note_events": true,
        "pipeline_events": true,
        "wiki_page_events": true,
        "job_events": true,
        "comment_on_event_enabled": true,
        "project_id": 1
    }"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 5, request)


@urlmatch(
    scheme="http", netloc="localhost", path="/api/v4/projects/1/services", method="get",
)
def resp_get_active_services(url, request):
    """Mock for active Services GET response."""
    content = """[{
        "id": 100152,
        "title": "Pipelines emails",
        "slug": "pipelines-email",
        "created_at": "2019-01-14T08:46:43.637+01:00",
        "updated_at": "2019-07-01T14:10:36.156+02:00",
        "active": true,
        "commit_events": true,
        "push_events": true,
        "issues_events": true,
        "confidential_issues_events": true,
        "merge_requests_events": true,
        "tag_push_events": true,
        "note_events": true,
        "confidential_note_events": true,
        "pipeline_events": true,
        "wiki_page_events": true,
        "job_events": true,
        "comment_on_event_enabled": true,
        "project_id": 1
    }]"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 5, request)


@urlmatch(
    scheme="http",
    netloc="localhost",
    path="/api/v4/projects/1/pipeline_schedules$",
    method="post",
)
def resp_create_project_pipeline_schedule(url, request):
    """Mock for creating project pipeline Schedules POST response."""
    content = """{
    "id": 14,
    "description": "Build packages",
    "ref": "master",
    "cron": "0 1 * * 5",
    "cron_timezone": "UTC",
    "next_run_at": "2017-05-26T01:00:00.000Z",
    "active": true,
    "created_at": "2017-05-19T13:43:08.169Z",
    "updated_at": "2017-05-19T13:43:08.169Z",
    "last_pipeline": null,
    "owner": {
        "name": "Administrator",
        "username": "root",
        "id": 1,
        "state": "active",
        "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80&d=identicon",
        "web_url": "https://gitlab.example.com/root"
    }
}"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 5, request)


@urlmatch(
    scheme="http",
    netloc="localhost",
    path="/api/v4/projects/1/pipeline_schedules/14/play",
    method="post",
)
def resp_play_project_pipeline_schedule(url, request):
    """Mock for playing a project pipeline schedule POST response."""
    content = """{"message": "201 Created"}"""
    content = content.encode("utf-8")
    return response(200, content, headers, None, 5, request)


class TestProject(unittest.TestCase):
    """Base class for GitLab Project tests."""

    def setUp(self):
        self.gl = Gitlab(
            "http://localhost",
            private_token="private_token",
            ssl_verify=True,
            api_version="4",
        )
        self.project = self.gl.projects.get(1, lazy=True)


class TestProjectSnippets(TestProject):
    def test_list_project_snippets(self):
        title = "Example Snippet Title"
        visibility = "private"

        @urlmatch(
            scheme="http",
            netloc="localhost",
            path="/api/v4/projects/1/snippets",
            method="get",
        )
        def resp_list_snippet(url, request):
            content = """[{
            "title": "%s",
            "description": "More verbose snippet description",
            "file_name": "example.txt",
            "content": "source code with multiple lines",
            "visibility": "%s"}]""" % (
                title,
                visibility,
            )
            content = content.encode("utf-8")
            return response(200, content, headers, None, 25, request)

        with HTTMock(resp_list_snippet):
            snippets = self.project.snippets.list()
            self.assertEqual(len(snippets), 1)
            self.assertEqual(snippets[0].title, title)
            self.assertEqual(snippets[0].visibility, visibility)

    def test_get_project_snippets(self):
        title = "Example Snippet Title"
        visibility = "private"

        @urlmatch(
            scheme="http",
            netloc="localhost",
            path="/api/v4/projects/1/snippets/1",
            method="get",
        )
        def resp_get_snippet(url, request):
            content = """{
            "title": "%s",
            "description": "More verbose snippet description",
            "file_name": "example.txt",
            "content": "source code with multiple lines",
            "visibility": "%s"}""" % (
                title,
                visibility,
            )
            content = content.encode("utf-8")
            return response(200, content, headers, None, 25, request)

        with HTTMock(resp_get_snippet):
            snippet = self.project.snippets.get(1)
            self.assertEqual(snippet.title, title)
            self.assertEqual(snippet.visibility, visibility)

    def test_create_update_project_snippets(self):
        title = "Example Snippet Title"
        visibility = "private"

        @urlmatch(
            scheme="http",
            netloc="localhost",
            path="/api/v4/projects/1/snippets",
            method="put",
        )
        def resp_update_snippet(url, request):
            content = """{
            "title": "%s",
            "description": "More verbose snippet description",
            "file_name": "example.txt",
            "content": "source code with multiple lines",
            "visibility": "%s"}""" % (
                title,
                visibility,
            )
            content = content.encode("utf-8")
            return response(200, content, headers, None, 25, request)

        @urlmatch(
            scheme="http",
            netloc="localhost",
            path="/api/v4/projects/1/snippets",
            method="post",
        )
        def resp_create_snippet(url, request):
            content = """{
            "title": "%s",
            "description": "More verbose snippet description",
            "file_name": "example.txt",
            "content": "source code with multiple lines",
            "visibility": "%s"}""" % (
                title,
                visibility,
            )
            content = content.encode("utf-8")
            return response(200, content, headers, None, 25, request)

        with HTTMock(resp_create_snippet, resp_update_snippet):
            snippet = self.project.snippets.create(
                {
                    "title": title,
                    "file_name": title,
                    "content": title,
                    "visibility": visibility,
                }
            )
            self.assertEqual(snippet.title, title)
            self.assertEqual(snippet.visibility, visibility)
            title = "new-title"
            snippet.title = title
            snippet.save()
            self.assertEqual(snippet.title, title)
            self.assertEqual(snippet.visibility, visibility)


class TestProjectExport(TestProject):
    @with_httmock(resp_create_export)
    def test_create_project_export(self):
        export = self.project.exports.create()
        self.assertEqual(export.message, "202 Accepted")

    @with_httmock(resp_create_export, resp_export_status)
    def test_refresh_project_export_status(self):
        export = self.project.exports.create()
        export.refresh()
        self.assertEqual(export.export_status, "finished")

    @with_httmock(resp_create_export, resp_download_export)
    def test_download_project_export(self):
        export = self.project.exports.create()
        download = export.download()
        self.assertIsInstance(download, bytes)
        self.assertEqual(download, binary_content)


class TestProjectImport(TestProject):
    @with_httmock(resp_import_project)
    def test_import_project(self):
        project_import = self.gl.projects.import_project("file", "api-project")
        self.assertEqual(project_import["import_status"], "scheduled")

    @with_httmock(resp_import_status)
    def test_refresh_project_import_status(self):
        project_import = self.project.imports.get()
        project_import.refresh()
        self.assertEqual(project_import.import_status, "finished")

    @with_httmock(resp_import_github)
    def test_import_github(self):
        base_path = "/root"
        name = "my-repo"
        ret = self.gl.projects.import_github("githubkey", 1234, base_path, name)
        self.assertIsInstance(ret, dict)
        self.assertEqual(ret["name"], name)
        self.assertEqual(ret["full_path"], "/".join((base_path, name)))
        self.assertTrue(ret["full_name"].endswith(name))


class TestProjectRemoteMirrors(TestProject):
    @with_httmock(resp_get_remote_mirrors)
    def test_list_project_remote_mirrors(self):
        mirrors = self.project.remote_mirrors.list()
        self.assertIsInstance(mirrors, list)
        self.assertIsInstance(mirrors[0], ProjectRemoteMirror)
        self.assertTrue(mirrors[0].enabled)

    @with_httmock(resp_create_remote_mirror)
    def test_create_project_remote_mirror(self):
        mirror = self.project.remote_mirrors.create({"url": "https://example.com"})
        self.assertIsInstance(mirror, ProjectRemoteMirror)
        self.assertEqual(mirror.update_status, "none")

    @with_httmock(resp_create_remote_mirror, resp_update_remote_mirror)
    def test_update_project_remote_mirror(self):
        mirror = self.project.remote_mirrors.create({"url": "https://example.com"})
        mirror.only_protected_branches = True
        mirror.save()
        self.assertEqual(mirror.update_status, "finished")
        self.assertTrue(mirror.only_protected_branches)


class TestProjectServices(TestProject):
    @with_httmock(resp_get_active_services)
    def test_list_active_services(self):
        services = self.project.services.list()
        self.assertIsInstance(services, list)
        self.assertIsInstance(services[0], ProjectService)
        self.assertTrue(services[0].active)
        self.assertTrue(services[0].push_events)

    def test_list_available_services(self):
        services = self.project.services.available()
        self.assertIsInstance(services, list)
        self.assertIsInstance(services[0], str)

    @with_httmock(resp_get_service)
    def test_get_service(self):
        service = self.project.services.get("pipelines-email")
        self.assertIsInstance(service, ProjectService)
        self.assertEqual(service.push_events, True)

    @with_httmock(resp_get_service, resp_update_service)
    def test_update_service(self):
        service = self.project.services.get("pipelines-email")
        service.issues_events = True
        service.save()
        self.assertEqual(service.issues_events, True)


class TestProjectPipelineSchedule(TestProject):
    @with_httmock(
        resp_create_project_pipeline_schedule, resp_play_project_pipeline_schedule
    )
    def test_project_pipeline_schedule_play(self):
        description = "Build packages"
        cronline = "0 1 * * 5"
        sched = self.project.pipelineschedules.create(
            {"ref": "master", "description": description, "cron": cronline}
        )
        self.assertIsNotNone(sched)
        self.assertEqual(description, sched.description)
        self.assertEqual(cronline, sched.cron)

        play_result = sched.play()
        self.assertIsNotNone(play_result)
        self.assertIn("message", play_result)
        self.assertEqual("201 Created", play_result["message"])
