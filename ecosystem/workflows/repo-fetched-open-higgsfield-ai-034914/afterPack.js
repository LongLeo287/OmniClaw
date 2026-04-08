import { execSync } from 'child_process';
import path from 'path';

export default async function afterPack({ appOutDir, packager }) {
    if (packager.platform.name !== 'mac') return;

    const appPath = path.join(appOutDir, `${packager.appInfo.productName}.app`);
    console.log(`  • ad-hoc signing  path=${appPath}`);
    execSync(`codesign --deep --force --sign - "${appPath}"`, { stdio: 'inherit' });
    console.log(`  • ad-hoc signing complete`);
}
