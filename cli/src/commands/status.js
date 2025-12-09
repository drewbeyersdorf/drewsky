import chalk from 'chalk';
import boxen from 'boxen';
import fs from 'fs-extra';
import { getMetrics, readWorkflowFiles } from '../utils/file-helpers.js';

export async function statusCommand() {
  console.log(chalk.blue.bold('\n📊 drewsky Workflow Status\n'));

  // Check for .drewsky directory
  const drewskyExists = await fs.pathExists('.drewsky');

  if (!drewskyExists) {
    console.log(
      boxen(
        chalk.yellow.bold('⚠️  Not Initialized') + '\n\n' +
        chalk.white('This project has not been initialized with drewsky.\n\n') +
        chalk.dim('Run: ') + chalk.cyan('drewsky init') + chalk.dim(' to get started.'),
        {
          padding: 1,
          margin: 1,
          borderStyle: 'round',
          borderColor: 'yellow'
        }
      )
    );
    return;
  }

  // Check workflow files
  const files = await readWorkflowFiles();

  // Determine current phase
  let currentPhase = 'Ready';
  let phaseIcon = '🏁';
  let nextSteps = [];

  if (!files.research && !files.plan && !files.completion) {
    currentPhase = 'Ready';
    phaseIcon = '🏁';
    nextSteps = [
      'Run: drewsky research "<task>" to start',
      'Or manually create .research.md'
    ];
  } else if (files.research && !files.plan) {
    currentPhase = 'Research';
    phaseIcon = '🔍';
    nextSteps = [
      'Review .research.md findings',
      'Run: drewsky plan --from-research',
      'Or manually create .plan.md'
    ];
  } else if (files.plan && !files.completion) {
    currentPhase = 'Planning / Implementation';
    phaseIcon = '⚙️';
    nextSteps = [
      'Review .plan.md steps',
      'Get stakeholder approval',
      'Begin implementation',
      'Run: drewsky verify to check claims'
    ];
  } else if (files.completion) {
    currentPhase = 'Completed';
    phaseIcon = '✅';
    nextSteps = [
      'Review .completion-snapshot.md',
      'Archive completed work',
      'Start new task with: drewsky research'
    ];
  }

  // Display workflow state
  console.log(chalk.white('Current Phase: ') + chalk.yellow.bold(`${phaseIcon} ${currentPhase}\n`));

  // Display file status
  console.log(chalk.white.bold('Workflow Files:\n'));
  console.log(
    (files.research ? chalk.green('  ✓ ') : chalk.dim('  ○ ')) +
    chalk.white('.research.md') +
    (files.research ? chalk.dim(' (exists)') : chalk.dim(' (not found)'))
  );
  console.log(
    (files.plan ? chalk.green('  ✓ ') : chalk.dim('  ○ ')) +
    chalk.white('.plan.md') +
    (files.plan ? chalk.dim(' (exists)') : chalk.dim(' (not found)'))
  );
  console.log(
    (files.completion ? chalk.green('  ✓ ') : chalk.dim('  ○ ')) +
    chalk.white('.completion-snapshot.md') +
    (files.completion ? chalk.dim(' (exists)') : chalk.dim(' (not found)'))
  );

  // Display metrics
  const metrics = await getMetrics();
  if (metrics) {
    console.log(chalk.white.bold('\n\nProject Metrics:\n'));
    console.log(chalk.white('  Sessions: ') + chalk.yellow(metrics.sessions || 0));
    console.log(chalk.white('  Research phases: ') + chalk.yellow(metrics.researchPhases || 0));
    console.log(chalk.white('  Plans created: ') + chalk.yellow(metrics.plansCreated || 0));
    console.log(chalk.white('  Tasks completed: ') + chalk.yellow(metrics.tasksCompleted || 0));

    if (metrics.tokenSavings) {
      const savings = metrics.tokenSavings.savingsPercent || 0;
      console.log(chalk.white('  Token savings: ') + chalk.green(`${savings}%`));
    }
  }

  // Display next steps
  console.log(chalk.blue.bold('\n\n📌 Next Steps:\n'));
  nextSteps.forEach((step, index) => {
    console.log(chalk.white(`  ${index + 1}. ${step}`));
  });

  // Display workflow reminder
  console.log(
    boxen(
      chalk.cyan.bold('drewsky Workflow') + '\n\n' +
      chalk.dim('Research → Plan → Implement\n\n') +
      chalk.white('1. ') + chalk.yellow('drewsky research') + chalk.dim(' - TCREI validation\n') +
      chalk.white('2. ') + chalk.yellow('drewsky plan') + chalk.dim(' - Task/Progress ledgers\n') +
      chalk.white('3. ') + chalk.yellow('drewsky verify') + chalk.dim(' - Chain of Verification\n') +
      chalk.white('4. ') + chalk.yellow('drewsky status') + chalk.dim(' - Check progress'),
      {
        padding: 1,
        margin: 1,
        borderStyle: 'round',
        borderColor: 'cyan'
      }
    )
  );

  console.log(chalk.dim('\nFor help: drewsky --help\n'));
}
