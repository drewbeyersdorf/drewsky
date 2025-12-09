import fs from 'fs-extra';
import chalk from 'chalk';
import boxen from 'boxen';
import ora from 'ora';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export async function initCommand(projectName) {
  const targetDir = projectName || process.cwd();
  const drewskyDir = path.join(targetDir, '.drewsky');

  console.log(chalk.blue.bold('\n🚀 drewsky Framework Initialization\n'));

  // Check if already initialized
  if (await fs.pathExists(drewskyDir)) {
    console.log(chalk.yellow('⚠️  drewsky is already initialized in this directory'));
    console.log(chalk.gray(`   .drewsky/ directory exists at: ${drewskyDir}`));
    console.log();
    process.exit(0);
  }

  const spinner = ora('Creating drewsky structure...').start();

  try {
    // Create .drewsky directory
    await fs.ensureDir(drewskyDir);

    // Create subdirectories
    await fs.ensureDir(path.join(drewskyDir, 'templates'));

    // Copy template files
    const templatesDir = path.join(__dirname, '../templates');
    await fs.copy(templatesDir, path.join(drewskyDir, 'templates'));

    // Create config.json
    const config = {
      version: '0.1.0',
      created: new Date().toISOString(),
      settings: {
        confidenceThreshold: 70,
        atomicStepDuration: 30, // minutes
        contextWarning: 40, // percentage
        contextEmergency: 60 // percentage
      }
    };
    await fs.writeJSON(path.join(drewskyDir, 'config.json'), config, { spaces: 2 });

    // Create metrics.json
    const metrics = {
      sessions: 0,
      researchPhases: 0,
      plansCreated: 0,
      tasksCompleted: 0,
      verificationsRun: 0,
      claimsVerified: 0,
      claimsTotal: 0,
      avgConfidence: 0,
      tokenSavings: {
        before: 41000,
        after: 1500,
        savingsPercent: 96
      }
    };
    await fs.writeJSON(path.join(drewskyDir, 'metrics.json'), metrics, { spaces: 2 });

    spinner.succeed(chalk.green('drewsky structure created'));

    // Success message
    console.log();
    console.log(boxen(
      chalk.green.bold('✅ drewsky initialized successfully!\n\n') +
      chalk.white('Created:\n') +
      chalk.gray('  .drewsky/\n') +
      chalk.gray('    ├── templates/\n') +
      chalk.gray('    │   ├── research.template.md\n') +
      chalk.gray('    │   ├── plan.template.md\n') +
      chalk.gray('    │   └── completion.template.md\n') +
      chalk.gray('    ├── config.json\n') +
      chalk.gray('    └── metrics.json\n\n') +
      chalk.blue.bold('Next steps:\n') +
      chalk.white('  1. ') + chalk.cyan('drewsky research "your task"\n') +
      chalk.white('  2. ') + chalk.cyan('drewsky plan\n') +
      chalk.white('  3. ') + chalk.cyan('drewsky status'),
      {
        padding: 1,
        margin: 1,
        borderStyle: 'round',
        borderColor: 'blue'
      }
    ));

    console.log(chalk.gray('\n💡 Tip: Run ') + chalk.cyan('drewsky --help') + chalk.gray(' to see all commands\n'));

  } catch (error) {
    spinner.fail(chalk.red('Failed to initialize drewsky'));
    console.error(chalk.red(`\nError: ${error.message}`));
    process.exit(1);
  }
}
