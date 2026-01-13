import os

from model.FileMetadata import FileMetadata
import pathspec


class DocumentService:

    def load_files_by_folder(self, folder: str) -> [FileMetadata]:
        files: [FileMetadata] = []
        for root, _, filenames in os.walk(folder):
            for filename in filenames:
                files.append(FileMetadata(path=root, file_name=filename))
        print('Total files found:', len(files))
        gitignore_text = self.get_gitignore_content('~/git/glasspilot')
        return self.get_not_ignored_files(gitignore_text, files)

    def load_files_by_names(self, file_name: str) -> FileMetadata:
        if os.path.isfile(file_name):
            # os tool to get path and filename
            file = FileMetadata(path=os.path.dirname(file_name), file_name=os.path.basename(file_name))
            gitignore_text = self.get_gitignore_content('~/git/glasspilot')
            files = self.get_not_ignored_files(gitignore_text, [file])
            if files and len(files) > 0:
                return files[0]
        return None

    def get_not_ignored_files(self, gitignore_text: str, files: [FileMetadata]) -> [FileMetadata]:
        """
        Filter out files that are ignored by the .gitignore patterns.
        TODO: currently it does not work as expected, need to use relative paths from the root of the git repo.
        """
        lines = gitignore_text.splitlines()
        spec = pathspec.PathSpec.from_lines("gitwildmatch", lines)

        def filemetadata_to_path(fm: FileMetadata) -> str:
            p = os.path.join(fm.path, fm.file_name)
            # normalize and convert to POSIX style which gitignore patterns expect
            return os.path.normpath(p).replace(os.sep, "/")

        not_ignored = [f for f in files if not spec.match_file(filemetadata_to_path(f))]
        # exclude binary files
        # TODO: improve by using a library to detect binary files
        not_ignored = [f for f in not_ignored if os.path.splitext(f.file_name)[1] in ['.txt', '.md', '.py', '.java', '.js', '.json', '.yaml', '.yml', '.csv']]
        return not_ignored

    def get_gitignore_content(self, folder: str) -> str:
        gitignore_path = os.path.join(folder, ".gitignore")
        print('Reading .gitignore file from:', gitignore_path)
        if os.path.isfile(gitignore_path):
            with open(gitignore_path, "r") as f:
                return f.read()
        return ""


# singleton service
document_service = DocumentService()
