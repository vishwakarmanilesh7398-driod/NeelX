from android.package_manager import PackageManager

packages = PackageManager.list_packages()

print(f"\nFound {len(packages)} Packages\n")

for package in packages[:20]:
    print(package)